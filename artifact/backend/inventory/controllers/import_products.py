import json
import re

import numpy as np
import pandas as pd
from django.db import transaction

from inventory.models import SubCategories, Products, Categories


class ImportProducts:

    def __init__(self, file) -> None:
        self.file = file
        super().__init__()

    def start(self):
        data_frame = self.get_data_frame()
        p_data = {}
        for index, row in data_frame.iterrows():
            p_data["name"] = row["title"]
            p_data["item_id"] = row["_id"]
            p_data["full_description"] = row["discount"]
            p_data["primary_description"] = row["discount"]
            p_data["pid"] = row["pid"]
            p_data["url"] = row["url"]
            p_data["images"] = self.parse_images(row)
            p_data["category"] = self.parse_category(row)
            p_data["actual_price"] = self.parse_price(row["actual_price"])
            p_data["selling_price"] = self.parse_price(row["selling_price"])
            p_data["extra_details"] = json.dumps(row["product_details"])
            try:
                self.get_or_create_product(p_data)
            except Exception as e:
                print(p_data)
                raise e

    @classmethod
    def parse_images(cls, row):
        return re.sub("[\[ \]']", '', row["images"]).split(',')

    @classmethod
    def parse_category(cls, row):
        return {"parent": row["category"], "sub": row["sub_category"]}

    @classmethod
    def parse_price(cls, price):
        price = float(price.replace(",", "")) if type(price) is str else price
        return 0 if np.isnan(price) else price

    @classmethod
    def get_or_create_product(cls, data):
        with transaction.atomic():
            category = data.pop("category", None)
            product, created = Products.objects.update_or_create(
                item_id=data["item_id"],
                defaults=data
            )
            if created:
                parent_category = Categories.objects.get_or_create(
                    category=category["parent"]
                )[0]
                sub_category = SubCategories.objects.get_or_create(
                    category=category["sub"],
                    parent_category=parent_category
                )[0]
                product.category = sub_category
                product.save(update_fields=("category", ))

    def get_data_frame(self):
        return pd.read_excel(self.file)
