from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField
import uuid


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
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    sharing = models.ManyToManyField(get_user_model(), related_name='shared_notes', through='SharedWith')

    def __str__(self):
        return self.file_name


class SharedWith(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        unique_together = (('person', 'note'),)

    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    editor = models.BooleanField(default=False)

