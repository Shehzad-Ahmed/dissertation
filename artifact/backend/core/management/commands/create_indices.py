from django.core.management.base import BaseCommand

from core import es_client, INDEX_CLASSES


class Command(BaseCommand):

    help = 'Creates the Elasticsearch indices.'

    def handle(self, *args, **options):

        for IndexClass in INDEX_CLASSES.values():
            es_client.indices.create(
                index=IndexClass.index,
                body={
                    "settings": IndexClass.settings,
                    "mappings": IndexClass.mappings,
                }
            )
