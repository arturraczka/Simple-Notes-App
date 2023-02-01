from django.test import SimpleTestCase
from django.urls import reverse, resolve
from notes_engine.views import (
                        NoteListView,
                        NoteCreateView,
                        NoteDetailView,
                        NoteDeleteView,
                        NoteUpdateView,
                        )

class TestUrls(SimpleTestCase):

    pk = 5

    def test_note_list_url_resolves(self):
        url = reverse('note_list')
        self.assertEquals(resolve(url).func.view_class, NoteListView)

    def test_note_create_url_resolves(self):
        url = reverse('note_new')
        self.assertEquals(resolve(url).func.view_class, NoteCreateView)

    def test_note_detail_url_resolves(self):
        url = reverse('note_detail', kwargs = {'pk': self.pk})
        self.assertEquals(resolve(url).func.view_class, NoteDetailView)

    def test_note_delete_url_resolves(self):
        pk = 5
        url = reverse('note_delete', kwargs = {'pk': self.pk})
        self.assertEquals(resolve(url).func.view_class, NoteDeleteView)

    def test_note_update_url_resolves(self):
        pk = 5
        url = reverse('note_update', kwargs = {'pk': self.pk})
        self.assertEquals(resolve(url).func.view_class, NoteUpdateView)