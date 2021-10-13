#!/usr/bin/env python
"""Script to collect podcast stats.

Requires:

* Python 3.6+
* aiohttp
"""
import asyncio
import codecs
import os
import re
import sys

import aiohttp
import async_timeout


def get_name_and_url(fname):
    if not os.path.exists(fname):
        print(f'File not found: {fname}')
        return (None, None)

    if os.path.isdir(fname):
        print(f"Ignoring folder {fname} and it's contents")
        return (None, None)

    if not fname.endswith('.rst'):
        print(f'Not an rst file: {fname}')
        return (None, None)

    with codecs.open(fname, 'r', 'utf-8') as fd:
        for line in fd:
            match = re.match(r'^\.\. podcast:: (.*)$', line)
            if match:
                break
        else:
            print(f"File '{fname}' isn't about an episode!")
            return (None, None)

    archive_episode_name = match.groups()[0]
    url = f'https://archive.org/details/{archive_episode_name}&output=json'
    return (archive_episode_name, url)


def print_summary(stats):
    total = sum([v['downloads'] for v in stats.values()])
    average = float(total) / len(stats)

    def by_downloads(item):
        return item[1]['downloads']

    sorted_by_downloads = sorted(stats.items(), key=by_downloads)
    most_downloaded = sorted(
        sorted_by_downloads[-5:], key=by_downloads, reverse=True)
    least_downloaded = sorted_by_downloads[:5]

    summary = sorted(stats.items(), key=lambda i: int(i[0].split('-')[-1]))
    for name, data in summary:
        print(f'{name}: {data["downloads"]}')

    print()
    print(f'Top 5 most downloaded episode:')
    for episode in most_downloaded:
        print(f'  * {episode[0]} ({episode[1]["downloads"]})')
    print('Top 5 least downloaded episode:')
    for episode in least_downloaded:
        print(f'  * {episode[0]} ({episode[1]["downloads"]})')
    print(f'Total of Downloads: {total}'.format(total))
    print(f'Average of Downloads: {round(average, 2)}')


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
        if 'item' not in response:
            # The download information won't be present for episodes that were
            # just published.
            continue
        stats[name] = response.get('item', {})
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
