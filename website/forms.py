from django import forms
from .models import Note
from tinymce.widgets import TinyMCE

class NoteModelForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta: 
        model = Note
        fields = [
            'file_name',
            'folder',
            'public',
            'text',
        ]