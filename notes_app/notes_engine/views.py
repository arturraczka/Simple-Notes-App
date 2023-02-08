from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Note
from .forms import NoteCreateForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy


@method_decorator(login_required, name='dispatch')
class NoteListView(ListView):
    model = Note
    template_name = 'notes_engine/note_list.html'
    context_object_name = 'notes_app'
    paginate_by = 5

    def get_queryset(self):  # overriding method, w/o super call
        queryset = Note.objects.filter(user = self.request.user).order_by('-created')
        return queryset


@method_decorator(login_required, name='dispatch')
class NoteDetailView(UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'notes_engine/note_detail.html'

    def test_func(self):
        note = Note.objects.get(id=self.kwargs['pk'])
        return self.request.user == note.user


@method_decorator(login_required, name='dispatch')
class NoteCreateView(SuccessMessageMixin, CreateView):
    model = Note
    template_name = 'notes_engine/note_new.html'
    form_class = NoteCreateForm
    success_message = 'Note created!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class NoteDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Note
    template_name = 'notes_engine/note_delete.html'
    success_url = reverse_lazy('note_list')
    success_message = 'Note deleted!'

    def test_func(self):
        note = Note.objects.get(id=self.kwargs['pk'])
        return self.request.user == note.user


@method_decorator(login_required, name='dispatch')
class NoteUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Note
    template_name = 'notes_engine/note_update.html'
    form_class = NoteCreateForm
    success_message = 'Note updated!'

    def test_func(self):
        note = Note.objects.get(id=self.kwargs['pk'])
        return self.request.user == note.user
