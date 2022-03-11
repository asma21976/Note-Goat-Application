from ast import For
from urllib import request
from django.shortcuts import render
from django.views.generic import (
    TemplateView, CreateView, ListView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy

from .models import (
    Note, Folder
)

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView, FormView, View
from django.views.generic.edit import FormMixin
from django.template import loader
from website import models


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

    



class CreateNoteView(CreateView):
    template_name = 'create_note.html'
    model = Note
    fields = ('file_name', 'text', 'public')
    context_object_name = 'note'
    success_url = reverse_lazy('home')

