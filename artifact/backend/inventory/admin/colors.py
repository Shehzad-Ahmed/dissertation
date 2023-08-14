from django.contrib import admin

from inventory.models import Colors


class ColorsAdmin(admin.ModelAdmin):

    fields = ("name",)

    search_fields = ("name",)

    list_filter = ("name",)


admin.site.register(Colors, ColorsAdmin)
