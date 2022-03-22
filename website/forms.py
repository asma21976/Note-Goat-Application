from django import forms
from .models import Note

class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'file_name',
            'text',
            'folder',
            'creator'
        ]