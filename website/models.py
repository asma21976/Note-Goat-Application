from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
import uuid
import datetime

'''
This models.py file and accounts/models.py represent the database.
The models are the entities in the database
'''

'''
The folder model has a uuid primary key, a folder_name, and a creator.
The folder_name is a string.
The creator is the CustomUser who made the note
'''
class Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    folder_name = models.CharField(max_length=50, default="New Folder",)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.folder_name

'''
The note entity has a uuid primary key, id.
The file_name is the name of the note and the text is the text contained in the note.
The folder is the folder model that the note is inside.
The field, sharing represents the many to many relationship between notes and users
as a note can be shared with many users and a user can have many notes shared with them.
'''
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


'''
The purpose of this model is for the many to many relationship between notes and users for sharing
notes with users.
Each SharedWith model has a note and the person (user) that the note is shared with.
The editor field is True if the person is allowed to edit the note. If false the user can only view the note shared with them
'''
class SharedWith(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        unique_together = (('person', 'note'),)

    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    editor = models.BooleanField(default=False)

