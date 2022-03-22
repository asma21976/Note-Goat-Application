from django.urls import path
from .views import HomePageView, CreateNoteView, ListNotesView, NoteDeleteView, UpdateFolderView, NoteUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('note/create/', CreateNoteView.as_view(), name='create_note'),
    path('note/', ListNotesView.as_view(), name='list_notes'),
    path('note/<uuid:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('folder/<uuid:pk>/update/', UpdateFolderView.as_view(), name='folder_update'),
    path('note/<uuid:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
]
