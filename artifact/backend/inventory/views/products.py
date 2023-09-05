from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from core import es_client
from inventory.es_indices import ProductsIndex


class ProductsSearchViewSet(viewsets.ViewSet):

    @classmethod
    def extract_query_params(cls, query_params):
        return {
            "track_total_hits": True,
            "query": {
                "multi_match": {
                    "query": query_params.get("q", ""),
                    "fields": ["name", "primary_description", "secondary_description", "full_description"],
                    "operator": "or",
                    "zero_terms_query": "all",
                    "fuzziness": "AUTO",
                }
            }
        }

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            self._paginator = LimitOffsetPagination()
            self._paginator.request = self.request
            self._paginator.max_limit = 100
            self._paginator.offset = self._paginator.get_offset(self.request)
            self._paginator.limit = self._paginator.get_limit(self.request)
            if not self._paginator.limit:
                self._paginator.limit = 25
        return self._paginator

    def list(self, request, *args, **kwargs):
        response = es_client.search(
            index=ProductsIndex.index,
            body=self.extract_query_params(request.query_params),
            size=self.paginator.limit,
            from_=self.paginator.offset
        )
        return self.get_response(response)

    def get_response(self, es_response):
        self.paginator.count = es_response["hits"]["total"]["value"]
        return self.paginator.get_paginated_response(
            data=map(self.extract_source, es_response["hits"]["hits"])
        )

    @classmethod
    def extract_source(cls, document):
        return document["_source"]
