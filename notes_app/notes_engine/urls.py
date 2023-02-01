from django.urls import path, include
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('' , NoteListView.as_view() , name= 'note_list'),
    path('new/' , NoteCreateView.as_view() , name = 'note_new'),
    path('<int:pk>/' , NoteDetailView.as_view() , name= 'note_detail'),
    path('<int:pk>/delete/' , NoteDeleteView.as_view() , name = 'note_delete'),
    path('<int:pk>/update/' , NoteUpdateView.as_view() , name = 'note_update'),
]

