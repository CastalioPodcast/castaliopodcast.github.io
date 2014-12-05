#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Og Maciel & Eliézer Rezende'
SITENAME = u'Castálio Podcast'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'pt'

TAG_CLOUD_STEPS = 8
TAG_CLOUD_MAX_ITEMS = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_USE_SUMMARY = True

# Github Profile
GITHUB_URL = 'http://github.com/CastalioPodcast'

# Social widget
SOCIAL = (('@castaliopod', 'https://twitter.com/castaliopod'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pages']

THEME = './themes/pelican-bootstrap3'
PLUGIN_PATHS = ['./plugins', ]
PLUGINS = [
    'summary',
    'feed_summary',
    'sitemap',
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# Disqus configuration

BANNER = True
BANNER_SUBTITLE = u"Um podcast inspirado pra castálio!"
BANNER_BACKGROUND_GRADIENT = 'linear-gradient(#2a2a29, #1c1c1c)'
BANNER_IMAGE = '/images/castalio-podcast.jpg'
BANNER_IMAGE_HEIGHT = 250
