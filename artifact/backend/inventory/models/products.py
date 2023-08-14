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

    images = ArrayField(models.URLField(blank=True, default=""), default=list)

    category = models.ForeignKey("inventory.SubCategories", null=True, default=None, on_delete=models.DO_NOTHING)

    colors = models.ManyToManyField("inventory.Colors")

    actual_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    selling_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    extra_details = models.JSONField(default=list)

    class Meta:

        verbose_name = "Product"

        verbose_name_plural = "Products"
