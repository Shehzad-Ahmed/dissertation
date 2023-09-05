

class ProductsIndex:

    index = "products"

    settings = {}

    mappings = {
        "properties": {
            "id": {
                "type": "keyword", "index": False
            },
            "name": {"type": "text", "analyzer": "standard"},
            "primary_description": {"type": "text", "analyzer": "standard"},
            "secondary_description": {"type": "text", "analyzer": "standard"},
        }
    }
