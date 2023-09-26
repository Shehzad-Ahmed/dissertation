import csv
from functools import update_wrapper
from io import StringIO

import pandas
from django.contrib import admin, messages
from django.template.response import TemplateResponse
from django.urls import path

from inventory.admin.forms import ProductImportForm
from inventory.controllers import ImportProducts
from inventory.models import Products


class ProductsAdmin(admin.ModelAdmin):

    change_list_template = "admin/products/change_list.html"

    import_products_template = "admin/products/import_products.html"

    fields = ("name", "primary_description", "secondary_description", "deleted",
              "full_description", "item_id",  "url", "category", "colors", "images", "extra_details")

    readonly_fields = ("id", "created_on", "updated_on")

    search_fields = ("name", "primary_description", "secondary_description", "full_description",
                     "item_id",)

    list_filter = ("category", "colors")

    list_display = ("name", "created_on")

    expected_headers = {
        "Name",
    }

    def import_products(self, request, *args, **kwargs):
        """Action for importing products based on a XLSX file.

        :param Request request: The request object
        :return TemplateResponse: Contains the form and context
        """

        form = ProductImportForm(request.POST or None, request.FILES or None)
        errors = []

        context = {
            "form": form,
            "meta": self.model._meta,
            "errors": errors,
            "stats": None,
            "headers": self.expected_headers,
        }

        if request.POST and form.is_valid():

            _file = form.cleaned_data["import_file"]

            ImportProducts(_file).start()
            messages.success(request, "Products have been imported.")
        return TemplateResponse(request, [self.import_products_template], context)

    def get_urls(self):
        """Adding url for user imports.

        :returns list: Admin Urls + Custom Urls
        """
        urls = super().get_urls()

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        custom_urls = [
            path(
                r"import/",
                wrap(self.admin_site.admin_view(self.import_products)),
                name="api_products_import",
            )
        ]
        return custom_urls + urls


admin.site.register(Products, ProductsAdmin)
