from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):

    user_id = models.UUIDField(primary_key=True, default=uuid4)
    middle_name = models.CharField(_('middle name'), max_length=150, null=True, blank=True)

    def __str__(self):
        return self.username