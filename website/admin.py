from django.contrib import admin


from .models import Folder, Note, SharedWith

admin.site.register(Folder)
admin.site.register(Note)
admin.site.register(SharedWith)