

class ProductsIndex:

    index = "products"

    settings = {
        "index.default_pipeline": "set_document_indexed_creation_date",
        "index.max_result_window": 30000
    }

    pipeline_name = "set_document_indexed_creation_date"

    pipeline_body = {
        "description": "Set document indexed creation date",
        "processors": [
            {
                "script": {
                    "source": "ctx._indexed_at = new Date();"
                }
            }
        ]
    }

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
