from django.shortcuts import render
from django.views.generic import (
    TemplateView, CreateView, ListView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy

from .models import (
    Note, Folder
)

# Create your views here.

from django.views.generic import TemplateView

from website import models


class HomePageView(CreateView):
    template_name = 'homepage.html'
    model = Folder
    fields = ('folder_name',)
    context_object_name = 'folders'
    # queryset = Folder.objects.all()
    success_url = reverse_lazy('home')



class CreateNoteView(CreateView):
    template_name = 'create_note.html'
    model = Note
    fields = ('file_name', 'text', 'public')
    context_object_name = 'note'
    success_url = reverse_lazy('home')

