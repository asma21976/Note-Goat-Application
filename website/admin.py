from django.contrib import admin

from .models import Note, Folder, SharedWith

# Register your models here.

admin.site.register(Note)
admin.site.register(Folder)
admin.site.register(SharedWith)