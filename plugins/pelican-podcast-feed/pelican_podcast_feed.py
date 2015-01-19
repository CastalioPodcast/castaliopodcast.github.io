#!/usr/bin/env python
# encoding: utf-8

"""
iTunes Feed Generator for Pelican.
"""

from __future__ import unicode_literals


from jinja2 import Markup
from pelican import signals
from pelican.writers import Writer
from pelican.generators import Generator
from pelican.utils import set_date_tzinfo
from feedgenerator import Rss201rev2Feed
from feedgenerator.django.utils.feedgenerator import rfc2822_date

# These are the attributes we want to pass to iTunes.
# TODO: provide a link to documentation about expected attributes.
ITEM_ELEMENTS = (
    'title',
    'itunes:author',
    'itunes:subtitle',
    'itunes:summary',
    'itunes:image',
    'enclosure',
    'description',
    'link',
    'guid',
    'pubDate',
    'itunes:duration',
    )

DEFAULT_ITEM_ELEMENTS = {}
for key in ITEM_ELEMENTS:
    DEFAULT_ITEM_ELEMENTS[key] = None


class PodcastFeed(Rss201rev2Feed):
    """Helper class which generates the XML based in the global settings"""
    def __init__(self, *args, **kwargs):
        """Nice method docstring goes here"""
        super(PodcastFeed, self).__init__(*args, **kwargs)

    def set_settings(self, settings):
        """Helper function which just receives the podcast settings.
        :param settings: A dictionary with all the site settings.
        """
        self.settings = settings

    def rss_attributes(self):
        """Returns the podcast feed's attributes.

        :return: A dictionary containing the feed's attributes.
        """
        attrs = super(PodcastFeed, self).root_attributes()
        attrs['xmlns:itunes'] = "http://www.itunes.com/dtds/podcast-1.0.dtd"
        attrs['version'] = '2.0'
        return attrs

    def add_root_elements(self, handler):
        """Adds some basic but useful attributes for an iTunes feed.

        :param handler: A SimplerXMLGenerator instance.
        """
        super(PodcastFeed, self).add_root_elements(handler)

        # Adds a language root tag. Ex:
        #  <language>en</language>
        if 'PODCAST_FEED_LANGUAGE' in self.settings:
            handler.addQuickElement(
                'language', self.settings['PODCAST_FEED_LANGUAGE']
                )
        # Adds a copyright root tag. Ex:
        #  <copyright>℗ &© 2014 Hack 'n' Cast</copyright>
        if 'PODCAST_FEED_COPYRIGHT' in self.settings:
            handler.addQuickElement(
                'copyright', self.settings['PODCAST_FEED_COPYRIGHT']
                )
        # Adds a explicit content root tag. Ex:
        #  <itunes:explicit>No</itunes:explicit>
        if 'PODCAST_FEED_EXPLICIT' in self.settings:
            handler.addQuickElement(
                'itunes:explicit', self.settings['PODCAST_FEED_EXPLICIT']
                )
        # Adds a show subtitle root tag. Ex:
        #  <itunes:subtitle>The hacker podcast!</itunes:subtitle>
        if 'PODCAST_FEED_SUBTITLE' in self.settings:
            handler.addQuickElement(
                'itunes:subtitle', self.settings['PODCAST_FEED_SUBTITLE']
                )
        # Adds a author root tag. Ex:
        #  <itunes:author>John Doe</itunes:author>
        if 'PODCAST_FEED_AUTHOR' in self.settings:
            handler.addQuickElement(
                'itunes:author', self.settings['PODCAST_FEED_AUTHOR']
                )
        # Adds a podcast summary root tag. Ex:
        #  <itunes:summary>A podcast about... </itunes:summary>
        if 'PODCAST_FEED_SUMMARY' in self.settings:
            handler.addQuickElement(
                'itunes:summary', self.settings['PODCAST_FEED_SUMMARY']
                )
        # Adds a podcast logo image root tag. Ex:
        #  <itunes:image href="http://example.com/logo.jpg" />
        if 'PODCAST_FEED_IMAGE' in self.settings:
            handler.addQuickElement(
                'itunes:image', attrs={
                    'href': self.settings['PODCAST_FEED_IMAGE']
                    }
                )
        # Adds a feed owner root tag an some child tags. Ex:
        #  <itunes:owner>
        #    <itunes:name>John Doe</itunes:name>
        #    <itunes:email>john.doe@example.com</itunes:email>
        #  </itunes:owner>
        if ('PODCAST_FEED_OWNER_NAME' in self.settings and
                'PODCAST_FEED_OWNER_EMAIL' in self.settings):
            handler.startElement('itunes:owner', {})
            handler.addQuickElement(
                'itunes:name', self.settings['PODCAST_FEED_OWNER_NAME']
                )
            handler.addQuickElement(
                'itunes:email', self.settings['PODCAST_FEED_OWNER_EMAIL']
                )
            handler.endElement('itunes:owner')
        # Adds a show category root tag and some child tags. Ex:
        #  <itunes:category text="Technology">
        #   <itunes:category text="Gadgets"/>
        #  </itunes:category>
        if 'PODCAST_FEED_CATEGORY' in self.settings:
            categories = self.settings['PODCAST_FEED_CATEGORY']
            if type(categories) in (list, tuple):
                handler.startElement(
                    'itunes:category', attrs={'text': categories[0]}
                    )
                handler.addQuickElement(
                    'itunes:category', attrs={'text': categories[1]}
                    )
                handler.endElement('itunes:category')
            else:
                handler.addQuickElement(
                    'itunes:category', attrs={'text': categories}
                    )

    def add_item_elements(self, handler, item):
        """Adds a new element to the iTunes feed, using information from
        ``item`` to populate it with relevant information about the article.

        :param handler: A SimplerXMLGenerator instance
        :param item: The dict generated by iTunesWriter._add_item_to_the_feed

        """
        for key in DEFAULT_ITEM_ELEMENTS:
            # empty attributes will be ignored.
            if item[key] is None:
                continue
            if key == 'description':
                content = item[key]
                handler.startElement('description', {})
                if not isinstance(content, unicode):
                    content = unicode(content, handler._encoding)
                content = content.replace("<html><body>", "")
                handler._write(content)
                handler.endElement('description')
            elif type(item[key]) in (str, unicode):
                handler.addQuickElement(key, item[key])
            elif type(item[key]) is dict:
                handler.addQuickElement(key, attrs=item[key])


class iTunesWriter(Writer):
    """Writer class for our iTunes feed.  This class is responsible for
    invoking the PodcastFeed and writing the feed itself (using it's superclass
    methods)."""

    def __init__(self, *args, **kwargs):
        """Class initializer"""
        super(iTunesWriter, self).__init__(*args, **kwargs)

    def _create_new_feed(self, feed_type, context):
        """Helper function (called by the super class) which will initialize
        the PodcastFeed object."""
        self.context = context
        description = self.settings.get('PODCAST_FEED_SUMMARY', '')
        title = (self.settings.get('PODCAST_FEED_TITLE', '') or
                 context['SITENAME'])
        feed = PodcastFeed(
            title=title,
            link=("{0}/".format(self.site_url)),
            feed_url=None,
            description=description)
        feed.set_settings(self.settings)
        return feed

    def _add_item_to_the_feed(self, feed, item):
        """Performs an 'in-place' update of existing 'published' articles
        in ``feed`` by creating a new entry using the contents from the
        ``item`` being passed.
        This method is invoked by pelican's core.

        :param feed: A PodcastFeed instance.
        :param item: An article (pelican's Article object).

        """
        # Local copy of iTunes attributes to add to the feed.
        items = DEFAULT_ITEM_ELEMENTS.copy()

        # Link to the new article.
        #  http://example.com/episode-01
        items['link'] = '{0}/{1}'.format(self.site_url, item.url)

        # Title for the article.
        #  ex: <title>Episode Title</title>
        items['title'] = Markup(item.title).striptags()

        # Summary for the article. This can be obtained either from
        # a ``:description:`` or a ``:summary:`` directive.
        #  ex: <itunes:summary>In this episode... </itunes:summary>
        if hasattr(item, 'description'):
            items['itunes:summary'] = item.description
        else:
            items['itunes:summary'] = Markup(item.summary).striptags()

        items['description'] = "<![CDATA[{}]]>".format(
            Markup(item.summary)
            )

        # Date the article was last modified.
        #  ex: <pubDate>Fri, 13 Jun 2014 04:59:00 -0300</pubDate>
        items['pubDate'] = rfc2822_date(
            set_date_tzinfo(
                item.modified if hasattr(item, 'modified') else item.date,
                self.settings.get('TIMEZONE', None))
            )

        # Name(s) for the article's author(s).
        #  ex: <itunes:author>John Doe</itunes:author>
        if hasattr(item, 'author'):
            items['itunes:author'] = item.author.name

        # Subtitle for the article.
        #  ex: <itunes:subtitle>My episode subtitle</itunes:subtitle>
        if hasattr(item, 'subtitle'):
            items['itunes:subtitle'] = Markup(item.subtitle).striptags()

        # Ex:
        #  <itunes:image href="http://example.com/Episodio1.jpg" />
        if hasattr(item, 'image'):
            items['itunes:image'] = {
                'href': '{0}{1}'.format(self.site_url, item.image)}

        # Information about the episode audio.
        #  ex: <enclosure url="http://example.com/episode.m4a"
        #   length="872731" type="audio/x-m4a" />
        if hasattr(item, 'podcast'):
            enclosure = {'url': item.podcast}
            # Include the file size if available.
            if hasattr(item, 'length'):
                enclosure['length'] = item.length
            # Include the audio mime type if available...
            if hasattr(item, 'mimetype'):
                enclosure['type'] = item.mimetype
            else:
                # ... or default to 'audio/mpeg'.
                enclosure['type'] = 'audio/mpeg'
            items['enclosure'] = enclosure

        # Duration for the audio file.
        #  <itunes:duration>7:04</itunes:duration>
        if hasattr(item, 'duration'):
            items['itunes:duration'] = item.duration

        # Unique identifier for the episode.
        # Use a 'guid' if available...
        #  ex: <guid>http://example.com/aae20050615.m4a</guid>
        if hasattr(item, 'guid'):
            items['guid'] = item.guid
        # ... else, use the article's link instead.
        #  ex: <guid>http://example.com/episode-01</guid>
        else:
            items['guid'] = items['link']
        # Add the new article to the feed.
        feed.add_item(**items)


class PodcastFeedGenerator(Generator):
    """Generates an iTunes content by inspecting all articles and invokes the
    iTunesWriter object, which will write the itunes Feed."""

    def __init__(self, *args, **kwargs):
        """Starts a brand new feed generator."""
        super(PodcastFeedGenerator, self).__init__(*args, **kwargs)
        # Initialize the number of episodes and where to save the feed.
        self.episodes = []
        self.feed_path = self.settings.get('PODCAST_FEED_PATH', None)

    def generate_context(self):
        """Looks for all 'published' articles and add them to the episodes
        list."""
        if self.feed_path:
            for article in self.context['articles']:
                # Only 'published' articles with the 'podcast' metatag.
                if (article.status.lower() == "published" and
                        hasattr(article, 'podcast')):
                    self.episodes.append(article)

    def generate_output(self, writer):
        """Write out the iTunes feed to a file.

        :param writer: A ``Pelican Writer`` instance.
        """
        if self.feed_path:
            writer = iTunesWriter(self.output_path, self.settings)
            writer.write_feed(self.episodes, self.context, self.feed_path)


def get_generators(generators):
    """Module function invoked by the signal 'get_generators'."""
    return PodcastFeedGenerator


def register():
    """Registers the module function `get_generators`."""
    signals.get_generators.connect(get_generators)
