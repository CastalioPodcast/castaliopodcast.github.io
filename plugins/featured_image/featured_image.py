import six
from pelican import signals
from pelican.contents import Article, Page
from pelican.generators import ArticlesGenerator


def images_extraction(instance):
    if isinstance(instance, (Article, Page)):
        if 'image' in instance.metadata:
            image = instance.metadata['image']
            if not image.startswith('http') and not image.startswith('/'):
                image = '/{}'.format(image)
            instance.featured_image = image
        if 'image-alt' in instance.metadata:
            instance.featured_image_alt = instance.metadata['image-alt']
        else:
            instance.featured_image_alt = instance.title


def run_plugin(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                images_extraction(article)


def register():
    signals.all_generators_finalized.connect(run_plugin)
