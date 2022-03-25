from django.urls import path
from .views import (
    HomePageView, CreateNoteView, ListNotesView, NoteDeleteView, UpdateFolderView,
    NoteUpdateView, CreateFolderView, FolderDeleteView, WelcomeView, ListSharedWithView, CreateSharedWithView,
    SharedWithDeleteView, SharedWithUpdateView)

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('note/create/', CreateNoteView.as_view(), name='create_note'),
    path('note/', ListNotesView.as_view(), name='list_notes'),
    path('note/<uuid:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('note/<uuid:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
    path('folder/create/', CreateFolderView.as_view(), name='create_folder'),
    path('folder/<uuid:pk>/update/', UpdateFolderView.as_view(), name='folder_update'),
    path('folder/<uuid:pk>/delete/', FolderDeleteView.as_view(), name='folder_delete'),
    path('', WelcomeView.as_view(), name='welcome_page'),
    path('sharing/<uuid:pk>/list/', ListSharedWithView.as_view(), name='shared_with_list'),
    path('sharing/<uuid:pk>/edit/', SharedWithUpdateView.as_view(), name='shared_with_update'),
    path('sharing/create', CreateSharedWithView.as_view(), name='shared_with_create'),
    path('sharing/<uuid:pk>/delete/', SharedWithDeleteView.as_view(), name='shared_with_delete'),
]