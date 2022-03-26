from django import forms
from .models import Note, Folder, SharedWith
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
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
            'text',
        ]

class SharedNoteModelForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta: 
        model = Note
        fields = [
            'text',
        ]

class CreateSharedWithForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(CreateSharedWithForm, self).__init__(*args, **kwargs)
        self.fields['note'].queryset = Note.objects.filter(
            creator=self.request.user)
        self.fields['person'].queryset = CustomUser.objects.exclude(
            username = self.request.user.username)
    
    #person = forms.CharField(max_length=100)

    class Meta: 
        model = SharedWith
        fields = [
            'person',
            'note',
            'editor',
        ]