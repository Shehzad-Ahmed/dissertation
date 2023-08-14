from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class SubCategories(models.Model):

    parent_category = models.ForeignKey("inventory.Categories", on_delete=models.CASCADE)

    category = models.TextField()

    class Meta:

        verbose_name = "Sub Category"

        verbose_name_plural = "Sub Categories"

        unique_together = (("category", "parent_category"), )