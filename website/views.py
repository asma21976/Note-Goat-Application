from django.shortcuts import render
from django.views import generic
from django.views.generic import (
    TemplateView, CreateView, ListView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy

from .models import (
    Note,
)

# Create your views here.

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class CreateNoteView(CreateView):
    template_name = 'create_note.html'
    model = Note
    fields = ('file_name', 'text', 'public')
    context_object_name = 'note'
    success_url = reverse_lazy('home')


class ListNotesView(ListView):
    template_name = 'list_note.html'
    model = Note
    fields = ('file_name',)
    context_object_name = 'notes'


class NoteDeleteView(DeleteView):
    template_name = 'delete_note.html'
    model = Note
    fields = ('file_name',)
    success_url = reverse_lazy('list_notes')
    context_object_name = 'notes'
