import uuid

from django.db import models


class Note(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    file_name = models.CharField(max_length=50, default="New Note",)
    text = models.TextField(blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name

