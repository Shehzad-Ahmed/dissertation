from django.contrib.postgres.fields import ArrayField
from django.db import models

from core.models import Base


class Products(Base):

    name = models.TextField()

    primary_description = models.TextField(blank=True, default="")

    secondary_description = models.TextField(blank=True, default="")

    full_description = models.TextField(blank=True, default="")

    item_id = models.TextField(blank=True, default="")

    pid = models.TextField(blank=True, default="")

    url = models.URLField(blank=True, default="", max_length=1000)

    images = ArrayField(models.URLField(blank=True, default=""), default=list, blank=True)

    category = models.ForeignKey(
        "inventory.SubCategories", null=True, default=None, on_delete=models.DO_NOTHING, blank=True
    )

    colors = models.ManyToManyField("inventory.Colors", blank=True)

    actual_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    selling_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    extra_details = models.JSONField(default=list, blank=True)

    class Meta:

        verbose_name = "Product"

        verbose_name_plural = "Products"
