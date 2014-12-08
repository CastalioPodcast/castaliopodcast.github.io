# -*- coding: utf-8 -*-

##### Feed example
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
#   <channel>
#       <title>Tudo sobre tudo</title>
#       <link>http://www.example.com/podcasts/everything/index.html</link>
#       <language>en-us</language>
#       <copyright>&#x2117; &amp; &#xA9; 2005 John Doe &amp; Family</copyright>
#       <itunes:subtitle>A show about everything</itunes:subtitle>
#       <itunes:author>John Doe</itunes:author>
#       <itunes:summary>
#           Tudo sobre tudo é um programa sobre tudo. A cada semana
#           abordaremos um assunto que será esmiuçado o máximo possível. Procure o
#           nosso podcast na iTunes Store
#       </itunes:summary>
#       <description>
#           Tudo sobre tudo é um programa sobre tudo. A cada semana abordaremos
#           um assunto que será esmiuçado o máximo possível. Procure o nosso
#           podcast na iTunes Store
#       </description>
#       <itunes:owner>
#           <itunes:name>John Doe</itunes:name>
#           <itunes:email>john.doe@example.com</itunes:email>
#       </itunes:owner>
#       <itunes:image href="http://example.com/podcasts/everything/Tudosobretudo.jpg" />
#       <itunes:category text="Tecnologia">
#           <itunes:category text="Gadgets"/>
#       </itunes:category>
#       <itunes:category text="TV e Filme"/>
#       <item>
#           <title>Chaves e mais chaves</title>
#           <itunes:author>Jane Doe</itunes:author>
#           <itunes:subtitle>
#               É muito divertido comparar os diferentes tipos de chaves dinamométricas!
#           </itunes:subtitle>
#           <itunes:summary>
#               Esta semana falaremos sobre as chaves dinamométricas que
#               utilizam o sistema métrico e as que utilizam o sistema inglês.
#               Qual é a melhor? Você precisa mesmo dos dois tipos? Veja aqui
#               respostas para as suas dúvidas.
#           </itunes:summary>
#           <itunes:image href="http://example.com/podcasts/everything/Tudosobretudo/Episodio2.jpg" />
#           <enclosure url="http://example.com/podcasts/everything/TudosobretudoEpisodio2.mp3" length="5650889" type="audio/mpeg" />
#           <guid>http://example.com/podcasts/archive/aae20050608.mp3</guid&
#           <pubDate>Qua, 8 Jun 2005 19:00:00 GMT</pubDate>
#           <itunes:duration>4:34</itunes:duration>
#       </item>
#   </channel>
# </rss>

from __future__ import unicode_literals

import six
if not six.PY3:
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from jinja2 import Markup
from pelican import signals
from pelican.writers import Writer
from pelican.generators import Generator
from pelican.utils import set_date_tzinfo
from feedgenerator import Rss201rev2Feed
from feedgenerator.django.utils.feedgenerator import rfc2822_date

ITEM_ELEMENTS = (
        'title',
        'itunes:author',
        'itunes:subtitle',
        'itunes:summary',
        'itunes:image',
        'enclosure',
        'guid',
        'pubDate',
        'itunes:duration',
        )

DEFAULT_ITEM_ELEMENTS = {}
for key in ITEM_ELEMENTS:
    DEFAULT_ITEM_ELEMENTS[key] = None

class iTunesFeed(Rss201rev2Feed):
    def __init__(self, *args, **kwargs):
        super(iTunesFeed, self).__init__(*args, **kwargs)

    def set_settings(self, settings):
        self.settings = settings

    def rss_attributes(self):#{{{
        attrs = super(iTunesFeed, self).root_attributes()
        attrs['xmlns:itunes'] = "http://www.itunes.com/dtds/podcast-1.0.dtd"
        attrs['version'] = '2.0'
        return attrs
    #}}}

    def add_root_elements(self, handler):#{{{
        super(iTunesFeed, self).add_root_elements(handler)
        if 'ITUNES_FEED_LANGUAGE' in self.settings:
            handler.addQuickElement('language', self.settings['ITUNES_FEED_LANGUAGE'])

        if 'ITUNES_FEED_COPYRIGHT' in self.settings:
            handler.addQuickElement('copyright', self.settings['ITUNES_FEED_COPYRIGHT'])

        if 'ITUNES_FEED_EXPLICIT' in self.settings:
            handler.addQuickElement('itunes:explicit', self.settings['ITUNES_FEED_EXPLICIT'])

        if 'ITUNES_FEED_SUBTITLE' in self.settings:
            handler.addQuickElement('itunes:subtitle', self.settings['ITUNES_FEED_SUBTITLE'])

        if 'ITUNES_FEED_AUTHOR' in self.settings:
            handler.addQuickElement('itunes:author', self.settings['ITUNES_FEED_AUTHOR'])

        if 'ITUNES_FEED_SUMMARY' in self.settings:
            handler.addQuickElement('itunes:summary', self.settings['ITUNES_FEED_SUMMARY'])

        if 'ITUNES_FEED_IMAGE' in self.settings:
            handler.addQuickElement('itunes:image', attrs={'href':self.settings['ITUNES_FEED_IMAGE']})

        if 'ITUNES_FEED_OWNER_NAME' in self.settings and 'ITUNES_FEED_OWNER_EMAIL' in self.settings:
            handler.startElement('itunes:owner', {})
            handler.addQuickElement('itunes:name', ['ITUNES_FEED_OWNER_NAME'])
            handler.addQuickElement('itunes:email', ['ITUNES_FEED_OWNER_EMAIL'])
            handler.endElement('itunes:owner')

        if 'ITUNES_FEED_CATEGORY' in self.settings:
            categories = self.settings['ITUNES_FEED_CATEGORY']
            if type(categories) in (list, tuple):
                handler.startElement('itunes:category', attrs={'text':categories[0]})
                handler.addQuickElement('itunes:category', attrs={'text':categories[1]})
                handler.endElement('itunes:category')
            else:
                handler.addQuickElement('itunes:category', attrs={'text':categories})
        #}}}

    def add_item_elements(self, handler, item):
        for key in DEFAULT_ITEM_ELEMENTS:
            if item[key] is None:
                continue
            if type(item[key]) in (str, unicode):
                handler.addQuickElement(key, item[key])
            elif type(item[key]) is dict:
                handler.addQuickElement(key, attrs=item[key])
            else:
                print 'Ignoring', item[key]


class iTunesWriter(Writer):
    def __init__(self, *args, **kwargs):
        super(iTunesWriter, self).__init__(*args, **kwargs)

    def _create_new_feed(self, feed_type, context):
        self.context = context
        sitename = Markup(context['SITENAME']).striptags()
        description = self.settings.get('ITUNES_FEED_SUMMARY', '')
        title = self.settings.get('ITUNES_FEED_TITLE', '')
        feed = iTunesFeed(
            title=title,
            link=(self.site_url + '/'),
            feed_url=None,
            description=description)
        feed.set_settings(self.settings)
        return feed

    def _add_item_to_the_feed(self, feed, item):
        items = DEFAULT_ITEM_ELEMENTS.copy()
        items['link'] = '%s/%s' % (self.site_url, item.url)

        # <title>Misture bem todos os seus temperos</title>
        items['title'] = Markup(item.title).striptags()

        # <itunes:summary>Esta semana falaremos sobre os moedores de sal e pimenta, comparando as porções despejadas, o material com que eles são feitos e a estética dos mesmos em geral. Venha se deliciar com esta festa de sabores!</itunes:summary>
        if hasattr(item, 'description'):
            items['itunes:summary'] = item.description
        else:
            items['itunes:summary'] = Markup(item.summary).striptags()
        items['description'] = items['itunes:summary']

        # <pubDate>Qua, 15 Jun 2005 19:00:00 GMT</pubDate>
        items['pubDate'] = rfc2822_date(set_date_tzinfo(item.modified if hasattr(item, 'modified') else item.date, self.settings.get('TIMEZONE', None)))
        # <itunes:author>John Doe</itunes:author>
        if hasattr(item, 'author'):
            items['itunes:author'] = item.author.name

        # <itunes:subtitle>A short primer on table spices</itunes:subtitle>
        if hasattr(item, 'subtitle'):
            items['itunes:subtitle'] = Markup(item.subtitle).striptags()

        # <itunes:image href="http://example.com/podcasts/everything/Tudosobretudo/Episodio1.jpg" />
        if hasattr(item, 'image'):
            items['itunes:image'] = {'href':self.site_url + item.image}

        # <enclosure url="http://example.com/podcasts/everything/TudosobretudoEpisodio3.m4a" length="8727310" type="audio/x-m4a" />
        if hasattr(item, 'podcast'):
            enclosure = {'url': item.podcast}
            if hasattr(item, 'length'):
                enclosure['length'] = item.length
            if hasattr(item, 'mimetype'):
                enclosure['type'] = item.mimetype
            else:
                enclosure['type'] = 'audio/mpeg'
            items['enclosure'] = enclosure

        # <itunes:duration>7:04</itunes:duration>
        if hasattr(item, 'duration'):
            items['itunes:duration'] = item.duration

        # <guid>http://example.com/podcasts/archive/aae20050615.m4a</guid>
        if hasattr(item, 'guid'):
            items['guid'] = item.guid
        else:
            items['guid'] = items['link']
        feed.add_item(**items)

class iTunesGenerator(Generator):
    def __init__(self, *args, **kwargs):
        super(iTunesGenerator, self).__init__(*args, **kwargs)
        self.episodes = []
        self.feed_path = self.settings.get('ITUNES_FEED_PATH', None)

    def generate_context(self):
        if self.feed_path:
            for article in self.context['articles']:
                if article.status.lower() == "published" and hasattr(article, 'podcast'):
                    self.episodes.append(article)

    def generate_output(self, writer):
        if self.feed_path:
            writer = iTunesWriter(self.output_path, self.settings)
            writer.write_feed(self.episodes, self.context, self.feed_path)

def get_generators(generators):
    return iTunesGenerator

def register():
    signals.get_generators.connect(get_generators)
