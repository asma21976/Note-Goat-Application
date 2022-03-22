from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import (
    TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from .forms import NoteModelForm

from .models import (
    Note,
)

# Create your views here.

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class CreateNoteView(CreateView):
    template_name = 'create_note.html'
    form_class = NoteModelForm
    queryset = Note.objects.all()


class ListNotesView(ListView):
    template_name = 'list_note.html'
    model = Note
    fields = ('file_name',)
    context_object_name = 'notes'

# class NoteDetailView(DetailView):
#     template_name = 'note_detail.html'

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Note, id=id_)

class NoteUpdateView(UpdateView):
    template_name = 'create_note.html' #temp.
    form_class = NoteModelForm
    queryset = Note.objects.all()


class NoteDeleteView(DeleteView):
    template_name = 'delete_note.html'
    model = Note
    fields = ('file_name',)
    success_url = reverse_lazy('list_notes')
    context_object_name = 'notes'
