from django.db import models

from core.models import Base


class Products(Base):

    name = models.TextField(unique=True)

    primary_description = models.TextField(blank=True, default="")

    secondary_description = models.TextField(blank=True, default="")

    full_description = models.TextField(blank=True, default="")

    item_id = models.TextField(blank=True, default="")

    url = models.URLField(blank=True, default="")

    category = models.ForeignKey("inventory.Categories", null=True, default=None, on_delete=models.DO_NOTHING)

    colors = models.ManyToManyField("inventory.Colors")

    class Meta:

        verbose_name = "Product"

        verbose_name_plural = "Products"
