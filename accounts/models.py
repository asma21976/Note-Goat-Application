from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

'''
The CustomUser entity should have all the fields of an AbstractUser as well as the additional
field, id, which is a uuid, to be used as the primary key.
'''
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username
