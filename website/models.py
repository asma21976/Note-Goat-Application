from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField
import uuid
import datetime


class Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    folder_name = models.CharField(max_length=50, default="New Folder", unique=True)

    def __str__(self):
        return self.folder_name


class Note(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    file_name = models.CharField(max_length=50, default="New Note",)
    text = models.TextField(blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name


class Address(models.Model):
    # this a superclass to be subclassed by any model with an address
    # but is not a relation itself
    class Meta:
        abstract = True

    address_line_1 = models.CharField(max_length=40, blank=True)
    address_line_2 = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40, blank=True)
    province_state = models.CharField('Province/State', max_length=40, blank=True)
    postal_code = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=True)
