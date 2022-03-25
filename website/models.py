from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
import uuid
import datetime

class Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    folder_name = models.CharField(max_length=50, default="New Folder",)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.folder_name


class Note(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    file_name = models.CharField(max_length=50, default="New Note",)
    text = models.TextField(blank=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    sharing = models.ManyToManyField(get_user_model(), related_name='shared_notes', through='SharedWith')

    # created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.file_name


class SharedWith(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        unique_together = (('person', 'note'),)

    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    editor = models.BooleanField(default=False)

