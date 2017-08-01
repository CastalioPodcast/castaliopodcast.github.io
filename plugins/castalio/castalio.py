# coding: utf-8
from docutils import nodes
from docutils.parsers.rst import directives, roles, Directive


class YouTubeEmbed(Directive):
    """Embed a YouTube video.

    Usage::

        .. youtube:: <video-id>
    """
    required_arguments = 1

    def run(self):
        content = u"""
        <p class="clearfix">
        <div class="embed-responsive embed-responsive-16by9">
            <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/{}" allowfullscreen></iframe>
        </div>
        </p>
        """.format(self.arguments[0])
        return [nodes.raw('', content, format='html')]

def register():
    directives.register_directive('youtube', YouTubeEmbed)
