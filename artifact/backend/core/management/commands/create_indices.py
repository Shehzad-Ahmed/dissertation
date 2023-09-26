from django.core.management.base import BaseCommand

from core import es_client, INDEX_CLASSES


class Command(BaseCommand):

    help = 'Creates the Elasticsearch indices.'

    def handle(self, *args, **options):

        for IndexClass in INDEX_CLASSES.values():
            es_client.ingest.put_pipeline(
                id=IndexClass.pipeline_name,
                body=IndexClass.pipeline_body
            )
            es_client.indices.create(
                index=IndexClass.index,
                body={
                    "settings": IndexClass.settings,
                    "mappings": IndexClass.mappings,
                }
            )
