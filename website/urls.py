from django.urls import path
from .views import HomePageView, CreateNoteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('note/create/', CreateNoteView.as_view(), name='create_note'),
]
