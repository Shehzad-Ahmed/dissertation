

class ProductsIndex:

    index = "products"

    settings = {}

    mappings = {
        "properties": {
            "id": {
                "type": "keyword", "index": False
            },
            "name": {"type": "text"},
        }
    }

