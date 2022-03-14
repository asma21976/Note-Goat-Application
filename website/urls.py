from django.urls import path
from .views import HomePageView, CreateNoteView, ListNotesView, NoteDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('note/create/', CreateNoteView.as_view(), name='create_note'),
    path('note/', ListNotesView.as_view(), name='list_notes'),
    path('note/<uuid:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
