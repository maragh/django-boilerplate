from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import get_current_timezone_name
from django.utils.translation import gettext_lazy as _
from pytz import common_timezones


class User(AbstractUser):
    COMMON_TIMEZONES = [(zone, zone) for zone in common_timezones]

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    active = models.BooleanField(_("active"), default=False)
    organizer = models.BooleanField(_("organizer"), default=False)
    agreed_to_terms = models.BooleanField(_("agreed to terms"), default=False)
    timezone = models.CharField(
        choices=COMMON_TIMEZONES, default=get_current_timezone_name, max_length=100
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)
    EMAIL_FIELD = "email"
