from elasticsearch import Elasticsearch
from core import settings
from inventory.es_indices import ProductsIndex

INDEX_CLASSES = {ProductsIndex.index: ProductsIndex}

es_client = Elasticsearch(settings.ELASTICSEARCH["URL"])
