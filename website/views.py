from ast import For
from urllib import request
from django.shortcuts import render
from django.views import generic
from django.views.generic import (
    TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView, FormView, View
)
from django.urls import reverse_lazy
from .forms import NoteModelForm

from .models import (
    Note, Folder,
)

# Create your views here.

from django.http import HttpResponse
# from django.views.generic import TemplateView, DetailView, ListView, FormView, View
from django.views.generic.edit import FormMixin
from django.template import loader
from website import models

class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        notes = []
        print("start Args")
        print(args)
        print("end Args")
        if args:
            notes = Note.objects.filter(folder=args[0])
            print("Here")
        else:
            notes = Note.objects.filter(folder='d435ab9e-086d-4d1b-89d8-0843a8377a47')
        folders = Folder.objects.all()
        template = loader.get_template('homepage.html')
        print(notes)
        context = {
            'folders': folders,
            'notes': notes
        }
        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        print(request.POST['id'])
        print(kwargs)
        return self.get(request, request.POST['id'], **kwargs)

class ListNotesView(ListView):
    template_name = 'list_note.html'
    model = Note
    fields = ('file_name',)
    context_object_name = 'notes'

class CreateNoteView(CreateView):
    template_name = 'create_note.html'
    model = Note
    fields = ('file_name', 'text', 'folder','public')
    context_object_name = 'note'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UpdateView):
    template_name = 'create_note.html' #temp.
    form_class = NoteModelForm
    queryset = Note.objects.all()
    model = Note
    success_url = reverse_lazy('list_notes')
    context_object_name = 'notes'

class NoteDeleteView(DeleteView):
    template_name = 'delete_note.html'
    model = Note
    fields = ('file_name',)
    success_url = reverse_lazy('list_notes')
    context_object_name = 'notes'

class CreateFolderView(CreateView):
    template_name = 'create_folder.html'
    model = Folder
    fields = ('folder_name',)
    success_url = reverse_lazy('home')

class UpdateFolderView(UpdateView):
    template_name = 'update_folder.html'
    model = Folder
    fields = ['folder_name']
    template_name_suffix = '_update_folder_form'

class FolderDeleteView(DeleteView):
    template_name = 'delete_folder.html'
    model = Folder
    fields = ('folder_name',)
    success_url = reverse_lazy('home')
    context_object_name = 'folder'