#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Og Maciel, Elyézer Rezende & Bruno Rocha'
SITENAME = u'Castálio Podcast'
SITEURL = 'http://castalio.info'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'pt'
LANG = u'pt_BR.UTF-8'
LOCALE = u'pt_BR'
CC_LICENSE = u'CC-BY-NC-SA'

# Sets Tagcloud usage
TAG_CLOUD_STEPS = 8
TAG_CLOUD_MAX_ITEMS = 150
DISPLAY_TAGS_INLINE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_USE_SUMMARY = True

# Github Profile
GITHUB_URL = 'http://github.com/CastalioPodcast'

# Social widget
SOCIAL = (
    ('GitHub', 'github', 'https://github.com/CastalioPodcast/CastalioPodcast.github.io'),
    ('Twitter', 'twitter', 'https://twitter.com/castaliopod'),
    ('Facebook', 'facebook', 'https://facebook.com/castaliopod'),
    ('iTunes', 'apple', 'https://itunes.apple.com/br/podcast/castalio-podcast/id446259197'),
    ('YouTube', 'youtube', 'http://youtube.com/castaliopodcast'),
    ('RSS Feed', 'rss', 'http://feeds.feedburner.com/CastalioPodcastMP3'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DIRECT_TEMPLATES = [
    'archives',
    'authors',
    'categories',
    'index',
    'search',
]
STATIC_PATHS = [
    'extra',
    'images',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

THEME = './themes/pelican-bootstrap3'
PLUGIN_PATHS = ['./plugins', ]
PLUGINS = [
    'castalio',
    'caster',
    'featured_image',
    'feed_summary',
    'pelican-podcast-feed',
    'sitemap',
    'summary',
    'tipue_search',
]
SUMMARY_END_MARKER = "<!-- more -->"

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

SUBSCRIBE = [
    ('iTunes', 'https://itunes.apple.com/br/podcast/castalio-podcast/id446259197'),
    ('Pocket Casts', 'http://pca.st/castalio'),
    ('Podflix', 'https://podflix.com.br/castaliopodcast'),
    (None, None),
    ('FeedBurner (RSS Feed)', 'http://feeds.feedburner.com/CastalioPodcastMP3'),
    ('Spotify do Castálio', 'https://open.spotify.com/user/elyezermr/playlist/0PDXXZRXbJNTPVSnopiMXg'),
    ('YouTube', 'http://bit.ly/CanalCastalio'),
]

# Disqus configuration
DISQUS_SITENAME = 'castliopodcast'
GOOGLE_ANALYTICS = "UA-21449168-1"

# Dark navbar
BOOTSTRAP_NAVBAR_INVERSE = True

# Site banner in the sidebar
BANNER = True
BANNER_ALL_PAGES = True
BANNER_IMAGE = 'images/castalio-podcast.png'
BANNER_SUBTITLE = u'Um podcast inspirado prá castálio!'
BANNER_BACKGROUND_COLOR='#fff'
SITELOGO = 'images/navbar-logo.png'
SITELOGO_SIZE = 20
HIDE_SITENAME = True
HIDE_SIDEBAR = True
SIDEBAR_BRAND_SUBTITLE = u"Um podcast inspirado prá castálio!"
SIDEBAR_BRAND_IMAGE = 'images/castalio-podcast.png'
SIDEBAR_BRAND_IMAGE_HEIGHT = 300
FAVICON = 'images/favicon.ico'

# iTunes plugin settings
PODCAST_FEED_PATH = u'feeds/podcast.rss'
PODCAST_FEED_TITLE = u'Castálio Podcast'
PODCAST_FEED_EXPLICIT = u'No'
PODCAST_FEED_LANGUAGE = u'pt-br'
PODCAST_FEED_COPYRIGHT = u'&#x2117; &amp; &#xA9; 2011-{0} {1}'.format(
    datetime.now().year, AUTHOR)
PODCAST_FEED_SUBTITLE = u'Um podcast inspirado para castálio'
PODCAST_FEED_AUTHOR = u'Og Maciel'
PODCAST_FEED_SUMMARY = u''
PODCAST_FEED_IMAGE = 'http://castalio.info/images/castalio-podcast-square.png'
PODCAST_FEED_OWNER_NAME = 'Og Maciel'
PODCAST_FEED_EMAIL_EMAIL = ''
PODCAST_FEED_CATEGORY = ['Technology', 'Podcasting']

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Show author name
SHOW_ARTICLE_AUTHOR = True

# Show comments count
DISQUS_DISPLAY_COUNTS = True

# Show article info in the index
DISPLAY_ARTICLE_INFO_ON_INDEX = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Sobre', '/sobre-o-castalio.html'),
    ('Agenda', '/agenda.html'),
    ('Episódios', '/archives.html'),
    ('Episodes', '/tag/english.html'),
    ('YouTube', '/youtube.html')
)
