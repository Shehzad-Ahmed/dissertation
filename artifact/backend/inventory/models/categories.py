from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Categories(models.Model):

    category = models.TextField()

    class Meta:

        verbose_name = "category"

        verbose_name_plural = "categories"

        constraints = [
            UniqueConstraint(
                Lower('category'),
                name='categories_category_unique',
            ),
        ]
