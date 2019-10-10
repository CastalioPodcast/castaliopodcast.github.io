import json
import os

import pelican
from docutils import nodes
from docutils.parsers.rst import directives, roles, Directive


TOP5_DATA = {}


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


class Top5(Directive):
    has_content = True
    _header_title = 'Top 5'
    _li_template = """<li>
    <strong>{category}:</strong>
    <a class="reference external" href="{url}">{name}</a>
    </li>
    """
    _category_text = {
        'book': 'Livro',
        'movie': 'Filme',
        'music': 'Música',
    }

    def run(self):
        if not self.content:
            error = self.state_machine.reporter.error(
                f'The "{self.name}" directive is empty; content required.',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno
            )
            return [error]

        node = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, node)

        with open(
            os.path.join(os.path.dirname(__file__), 'top5.json'),
            encoding='utf-8'
        ) as fp:
            data = json.load(fp)

        bullet_list = nodes.bullet_list()
        for field in node[0]:
            category = field[0].astext()
            for item in [item.astext() for item in field[1][0]]:
                top5_item = data.get(category, {}).get(item)
                if top5_item:
                    bullet_list.children.append(nodes.raw(
                        '',
                        self._li_template.format(
                            category=self._category_text[category],
                            name=item,
                            url=top5_item['url'],
                        ),
                        format='html',
                    ))
        return [
            nodes.title(self._header_title, '', nodes.Text(self._header_title)),
            bullet_list,
        ]


def register():
    directives.register_directive('youtube', YouTubeEmbed)
    directives.register_directive('top5', Top5)
