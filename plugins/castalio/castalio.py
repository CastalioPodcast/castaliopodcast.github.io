import operator
import os

import pelican
import yaml
from docutils import nodes
from docutils.parsers.rst import directives, Directive


TOP5_STATS = {}


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
    final_argument_whitespace = True
    has_content = True
    optional_arguments = 1

    _header_title = 'Top 5'
    _li_template = """<li>
    <a class="reference external" href="{url}">{name}</a>
    </li>
    """
    _li_template_no_url = """<li>{name}</li>"""
    _category_text = {
        'app': 'Aplicativos',
        'beer': 'Cervejas',
        'book': 'Livros',
        'game': 'Games',
        'movie': 'Filmes',
        'music': 'Músicas',
        'pizza': 'Pizzas',
        'podcast': 'Podcasts',
        'site': 'Sites',
        'twitter': 'Twitters',
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
            os.path.join(os.path.dirname(__file__), 'top5.yaml'),
            encoding='utf-8'
        ) as fp:
            data = yaml.safe_load(fp)

        if self.arguments:
            header_title = self.arguments[0]
        else:
            header_title = self._header_title
        generated_nodes = [
            nodes.title(header_title, '', nodes.Text(header_title)),
        ]
        for field in node[0]:
            category = field[0].astext()
            if category not in TOP5_STATS:
                TOP5_STATS[category] = {}
            generated_nodes.append(
                nodes.raw(
                    '',
                    '<h3>' + self._category_text[category] + ':</h3>',
                    format='html'
                )
            )
            enumerated_list = nodes.enumerated_list()
            for item in [item.astext() for item in field[1][0]]:
                top5_item = data.get(category, {}).get(item)
                if top5_item is None:
                    return [self.state_machine.reporter.error(
                        f'The Top 5 "{item}" was not found.',
                        nodes.literal_block(self.block_text, self.block_text),
                        line=self.lineno
                    )]
                if 'url' in top5_item:
                    text = self._li_template.format(
                        name=item,
                        url=top5_item['url'],
                    )
                else:
                    text = self._li_template_no_url.format(
                        category=self._category_text[category],
                        name=item,
                    )
                enumerated_list.children.append(nodes.raw(
                    '',
                    text,
                    format='html',
                ))
                if item not in TOP5_STATS[category]:
                    TOP5_STATS[category][item] = {
                        'count': 0,
                        'name': item,
                        'url': top5_item.get('url'),
                    }
                TOP5_STATS[category][item]['count'] += 1
            generated_nodes.append(enumerated_list)
        return generated_nodes


class Top5Best(Directive):
    _li_template = """<li>
    <a class="reference external" href="{url}">{name}</a> ({count})
    </li>
    """
    _li_template_no_url = '<li>{name} ({count})</li>'
    _category_text = {
        'app': 'Top 5 Aplicativos',
        'beer': 'Top 5 Cervejas',
        'book': 'Top 5 Livros',
        'game': 'Top 5 Games',
        'movie': 'Top 5 Filmes',
        'music': 'Top 5 Músicas',
        'pizza': 'Top 5 Pizzas',
        'podcast': 'Top 5 Podcast',
        'site': 'Top 5 Sites',
        'twitter': 'Top 5 Twitters',
    }

    def run(self):
        output_nodes = []
        for category in TOP5_STATS:
            category_title = self._category_text[category]
            output_nodes.append(
                nodes.raw('', f'<h2>{category_title}</h2>', format='html')
            )
            items = sorted(
                TOP5_STATS[category].values(),
                key=operator.itemgetter('count'),
                reverse=True,
            )[:5]
            enumerated_list = nodes.enumerated_list()
            for item in items:
                if item['url']:
                    text = self._li_template.format(**item)
                else:
                    text = self._li_template_no_url.format(**item)
                enumerated_list.children.append(nodes.raw(
                    '',
                    text,
                    format='html',
                ))
            output_nodes.append(enumerated_list)
        return output_nodes


def finalize(pelican):
    # Clear the TOP5_STATS when pelican is done. This is useful when running
    # the dev server so it resets the counts
    TOP5_STATS.clear()


def register():
    directives.register_directive('top5', Top5)
    directives.register_directive('top5best', Top5Best)
    directives.register_directive('youtube', YouTubeEmbed)
    pelican.signals.finalized.connect(finalize)
