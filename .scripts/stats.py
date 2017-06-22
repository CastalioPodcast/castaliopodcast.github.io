#!/usr/bin/env python
# encoding: utf-8
"""Script to collect podcast stats.

Requires:

* Python 3.5+
* aiohttp
"""
import asyncio
import codecs
import json
import os
import re
import sys

import aiohttp
import async_timeout


def get_name_and_url(fname):
    if not os.path.exists(fname):
        print('File not found: {}'.format(fname))
        return (None, None)

    if os.path.isdir(fname):
        print("Ignoring folder {} and it's contents".format(fname))
        return (None, None)

    if not fname.endswith('.rst'):
        print('Not an rst file: {}'.format(fname))
        return (None, None)

    with codecs.open(fname, 'r', 'utf-8') as fd:
        for line in fd:
            match =  re.match("^\.\. podcast:: (.*)$", line)
            if match:
                break
        else:
            print("File '{}' isn't about an episode!".format(fname))
            return (None, None)

    archive_episode_name = match.groups()[0]
    url = "https://archive.org/details/{}&output=json".format(archive_episode_name)
    return (archive_episode_name, url)


def print_summary(stats):

    total = sum([v['downloads'] for v in stats.values()])
    average = float(total) / len(stats)
    most_downloaded = max(*stats.items(), key=lambda x:x[1]['downloads'])
    least_downloaded = min(*stats.items(), key=lambda x:x[1]['downloads'])

    episodegetter = lambda i: int(i[0].split('-')[-1])
    for name, data in sorted(stats.items(), key=episodegetter):
        print('{}: {}'.format(name, data['downloads']))

    print()
    print('Most downloaded episode: {} ({})'.format(
        most_downloaded[0], most_downloaded[1]['downloads']))
    print('Least downloaded episode: {} ({})'.format(
        least_downloaded[0], least_downloaded[1]['downloads']))
    print('Total of Downloads: {}'.format(total))
    print('Average of Downloads: {}'.format(round(average, 2)))

async def fetch(session, url):
    """Fetch an URL and returns its JSON response."""
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.json()

async def main(loop, data):
    stats = {}
    async with aiohttp.ClientSession(loop=loop) as session:
        responses = await asyncio.gather(*[
            loop.create_task(fetch(session, url)) for name, url in data])

    # By this time we have all responses and they are ordered the same order as
    # the tasks
    for name, response in zip([name for name, _ in data], responses):
        stats[name] = {
            'length': response['files']['/{}.ogg'.format(name)]['length'],
        }
        stats[name].update(response['item'])
    print_summary(stats)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Usage: {} <rst_file> ...".format(sys.argv[0]))
        exit(1)

    episodes = sorted(sys.argv[1:])
    data = [
        get_name_and_url(episode) for episode in episodes
        if episode[0] is not None
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, data))

    exit(0)
