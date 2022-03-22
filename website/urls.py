from django.contrib import admin
from django.urls import path
from .views import HomePageView, CreateNoteView, ListNotesView, NoteDeleteView, NoteUpdateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('note/create/', CreateNoteView.as_view(), name='create_note'),
    # path('note/<id:pk>', NoteDetailView.as_view(), name='note_detail'),
    path('note/view/', ListNotesView.as_view(), name='list_notes'),
    path('note/<uuid:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
    path('note/<uuid:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('admin/', admin.site.urls),
]
