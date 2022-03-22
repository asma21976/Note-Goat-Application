from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
