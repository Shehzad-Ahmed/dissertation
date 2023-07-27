from django.db import models


class Categories(models.Model):

    category = models.TextField()

    class Meta:

        verbose_name = "category"

        verbose_name_plural = "categories"
