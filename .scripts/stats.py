#!/usr/bin/env python
# encoding: utf-8

import re
import sys
import os
import urllib2
import json
import codecs

def print_summary(stats):
    total = sum(stats.values())
    average = float(total)/len(stats)
    most_downloaded = max(*stats.items(), key=lambda x:x[1])
    least_downloaded = min(*stats.items(), key=lambda x:x[1])

    print "\n"
    print "Most downloaded episode: {} ({})".format(*most_downloaded)
    print "Least downloaded episode: {} ({})".format(*least_downloaded)
    print "Total of Downloads: {}".format(total)
    print "Average of Downloads: {}".format(round(average, 2))


def print_stats(name, count):
    print "{}: {}".format(name, count)

def get_download_count(url):
    code = None
    try:
        connection = urllib2.urlopen(url)
        code = ''.join(connection.readlines())
        connection.close()
    except urllib2.HTTPError, e:
        print "Error reading %s"%url
    jobject = json.loads(code)
    return jobject['item']['downloads']

def get_name_and_url(fname):
    if not os.path.exists(fname):
        print "File not found: {}".format(fname)
        return (None, None)

    if os.path.isdir(fname):
        print "Ignoring folder {} and it's contents".format(fname)
        return (None, None)

    if not fname.endswith(".rst"):
        print "Not an rst file: {}".format(fname)
        return (None, None)

    with codecs.open(fname, 'r', 'utf-8') as fd:
        for line in fd:
            match =  re.match("^\.\. podcast:: (.*)$", line)

            if match:
                break
        else:
            print "File '{}' isn't about an episode!".format(fname)
            return (None, None)

    archive_episode_name = match.groups()[0]
    url = "https://archive.org/details/{}&output=json".format(archive_episode_name)
    return (archive_episode_name, url)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Usage: {} <rst_file> ...".format(sys.argv[0])
        exit(1)

    stats = {}
    episodes = sorted(sys.argv[1:])
    for episode in episodes:
        (name, url) = get_name_and_url(episode)
        if not url:
            continue
        count = get_download_count(url)
        stats[name] = count
        print_stats(name, count)
    if len(stats) > 2:
        print_summary(stats)
    exit(0)
