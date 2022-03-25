from django import forms
from .models import Note, Folder
from tinymce.widgets import TinyMCE

class NoteModelForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(NoteModelForm, self).__init__(*args, **kwargs)
        self.fields['folder'].queryset = Folder.objects.filter(
            creator=self.request.user)

    class Meta: 
        model = Note
        fields = [
            'file_name',
            'folder',
            'public',
            'text',
        ]