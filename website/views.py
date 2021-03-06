from ast import For
from urllib import request
from django.shortcuts import render
from django.views import generic
from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView, DetailView, View
)
from django.urls import reverse_lazy
from .forms import NoteModelForm, SharedNoteModelForm, CreateSharedWithForm

from .models import (
    Note, Folder, SharedWith
)

from django.http import HttpResponse
from django.views.generic.edit import FormMixin
from django.template import loader
from website import models
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime

'''
This view is for the welcome page
'''
class WelcomeView(TemplateView):
    template_name = 'welcome.html'

'''
This view is for the homepage
'''
class HomePageView(LoginRequiredMixin, View):
    def get_queryset(self):
        queryset = Folder.objects.filter(creator=self.request.user)
        return queryset

    def get_queryset(self):
        queryset = Note.objects.filter(creator=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        notes = []
        print("start Args")
        print(args)
        print("end Args")
        if args:
            notes = Note.objects.filter(folder=args[0])
            # notes = Note.objects.filter(creator=self.request.user)
            print("Here")
        else:
            notes = Note.objects.filter(folder='d435ab9e-086d-4d1b-89d8-0843a8377a47')
        folders = Folder.objects.filter(creator=self.request.user)
        shared_with = SharedWith.objects.filter(person=self.request.user)
        template = loader.get_template('homepage.html')
        print(notes)
        context = {
            'folders': folders,
            'notes': notes,
            'shared_with': shared_with,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        print(request.POST['id'])
        print(kwargs)
        return self.get(request, request.POST['id'], **kwargs)


'''
This view is for a user to create a note
'''
class CreateNoteView(LoginRequiredMixin, CreateView):
    def get_queryset(self):
        queryset = Note.objects.filter(creator=self.request.user)
        return queryset
      
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(CreateNoteView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    template_name = 'create_note.html'
    model = Note
    form_class = NoteModelForm
    context_object_name = 'notes'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


'''
This view is for a user to update a note that belongs to them
'''
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(NoteUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    template_name = 'update_note.html'
    form_class = NoteModelForm
    queryset = Note.objects.all()
    model = Note
    success_url = reverse_lazy('home')
    context_object_name = 'notes'


'''
This view is for a user to update a note that is shared with them
'''
class SharedNoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update_note.html'
    form_class = SharedNoteModelForm
    queryset = Note.objects.all()
    # fields = ("text",)
    model = Note
    success_url = reverse_lazy('home')
    context_object_name = 'notes'

'''
This view is for a user to delete one of their notes
'''
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_note.html'
    model = Note
    fields = ('file_name',)
    success_url = reverse_lazy('home')
    context_object_name = 'notes'


'''
This view is for a user to create a folder
'''
class CreateFolderView(LoginRequiredMixin, CreateView):
    template_name = 'create_folder.html'
    model = Folder
    fields = ('folder_name',)
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form) 

'''
This view is for a user to update the name of the folder
'''
class UpdateFolderView(LoginRequiredMixin, UpdateView):
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    template_name = 'update_folder.html'
    model = Folder
    fields = ['folder_name']
    #template_name_suffix = '_update_folder_form'
    success_url = reverse_lazy('home')
    context_object_name = 'folder'

'''
This view is for a user to delete one of their folders
'''
class FolderDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_folder.html'
    model = Folder
    fields = ('folder_name',)
    success_url = reverse_lazy('home')
    context_object_name = 'folder'


'''
This view is for a user to share a note with another user
'''
class CreateSharedWithView(LoginRequiredMixin, CreateView):
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(CreateSharedWithView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    template_name = 'shared_with/create.html'
    model = SharedWith
    # fields = ('person', 'note', 'editor',)
    form_class = CreateSharedWithForm
    queryset = SharedWith.objects.all()
    context_object_name = 'shared_with'
    success_url = reverse_lazy('home')

'''
This view is for a user to update whether or not a user that their note is shared with is an editor or not
'''
class SharedWithUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'shared_with/update.html'
    model = SharedWith
    fields = ('editor',)
    context_object_name = 'shared_with'
    success_url = reverse_lazy('home')


'''
This view is for a user to un-share a note with someone
'''
class SharedWithDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'shared_with/delete.html'
    model = SharedWith
    context_object_name = 'shared_with'
    success_url = reverse_lazy('home')


'''
This view is for a user to view all the users a note of theirs is shared with
'''
class ListSharedWithView(LoginRequiredMixin, DetailView):
    template_name = 'shared_with/list.html'
    model = Note
    context_object_name = 'shared_with_list'

    def get_context_data(self, **kwargs):
        ctx = super(ListSharedWithView, self).get_context_data(**kwargs)
        ctx['shared_with'] = SharedWith.objects.all()
        return ctx


'''
This view is for a user to view a note that is shared with them without being able to edit it
'''
class NoteView(LoginRequiredMixin, DetailView):
    template_name = 'view_shared_note.html'
    model = Note
    context_object_name = 'note'
