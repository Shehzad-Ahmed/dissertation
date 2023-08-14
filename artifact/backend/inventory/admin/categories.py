from django.contrib import admin

from inventory.models import Categories


class CategoriesAdmin(admin.ModelAdmin):

    fields = ("category", )

    search_fields = ("category",)

    list_filter = ("category",)


admin.site.register(Categories, CategoriesAdmin)
