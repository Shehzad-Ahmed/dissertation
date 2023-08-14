from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from core.managers.users import CustomUserManager
from core.models import Base


class Users(Base, AbstractUser):

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    date_of_birth = models.DateField(null=True)

    username = None

    EMAIL_FIELD = "email"

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:

        db_table = "users"

        verbose_name = "User"

        verbose_name_plural = "Users"
