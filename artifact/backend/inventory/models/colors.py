from django.db import models


class Colors(models.Model):

    name = models.TextField(unique=True)

    class Meta:

        verbose_name = "Color"

        verbose_name_plural = "Colors"
