# -*- coding: utf-8 -*-

"""Description"""

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class Podcast(Directive):
    """ Include podcast

    Usage:
    .. podcast:: TITLE
        :rss: link
        :itunes: link
    """

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'rss': str,
        'itunes': str,
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):


        title = self.arguments[0].strip()

        rss = u''
        itunes = u''

        if 'rss' in self.options:
            rss = self.options['rss']

        if 'itunes' in self.options:
            itunes = self.options['itunes']

        HTML = u"""
        <div class="podcast text-center">
            <iframe src="https://archive.org/embed/{title}/{title}.mp3" width="500" height="30" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>

            <div class="podcast-download">
                <span class="label label-success"><a href="https://archive.org/download/{title}/{title}.mp3"><i class="fa fa-download"></i> Download MP3</a></span>
                <span class="label label-success"><a href="https://archive.org/download/{title}/{title}.ogg"><i class="fa fa-download"></i> Download OGG</a></span>
                <span class="label label-success"><a href="https://archive.org/download/{title}/{title}.m4a"><i class="fa fa-download"></i> Download M4A</a></span>
            </div>
        </div>
        """.format(title=title, podcast_rss=rss, podcast_itunes=itunes)

        return [nodes.raw('', HTML, format='html')]


def register():
    directives.register_directive('podcast', Podcast)
