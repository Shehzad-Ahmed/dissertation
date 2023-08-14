import io

from django.test import TestCase


# Create your tests here.
from openpyxl import Workbook

from inventory.controllers import ImportProducts


class ImportProductsTestCases(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.create_excel_file()

    def create_excel_file(self):
        product = (
                "fa8e22d6-c0b6-5229-bb9e-ad52eda39a0a",  # _id
                "2,999",  # actual_price
                3.9,  # average rating
                "York",  # brand
                "Clothing and Accessories",  # category
                "02/10/2021, 20:11:51",  # crawted_at
                "Yorker trackpants made from 100 % rich combed cotton giving it a rich look.",  # discount
                "['https://ruk.flixcart.com/image/128/', 'https://ruk.flixcart.com/image/128/128/jr58l8w0/']",  # images
                "FALSE",  # out of stock
                "TKPFCZ9EA7H5FYZH",  # pid
                "[{'Style Code': '1005COMBO2'}, {'Closure': 'Elastic'}, {'Pockets': 'Side Pockets'}, "
                "{'Fabric': 'Cotton Blend'}, {'Pattern': 'Solid'}, {'Color': 'Multicolor'}]",  # product details
                "Shyam Enterprises",  # seller
                921,  # selling price
                "Bottomwear",  # sub category
                "Solid Men Multicolor Track Pants",  # title
                "https://www.flipkart.com/yorker-solid-men-multicolor-track-pants/p/itmd259?pid=TKPFCZ9",  # url
        )

        headers = [
            "_id", "actual_price",
            "average_rating", "brand",
            "category", "crawled_at", "discount",
            "images", "out_of_stock",
            "pid", "product_details",
            "seller", "selling_price",
            "sub_category", "title",
            "url"
        ]

        wb = Workbook()
        ws = wb.worksheets[0]
        ws.append(headers)
        ws.append(product)

        file_excel = io.BytesIO()
        wb.save(file_excel)
        self.file_excel = file_excel

    def test_import_products(self):

        im_pd = ImportProducts(self.file_excel)
        im_pd.start()
