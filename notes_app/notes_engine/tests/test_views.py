from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from notes_engine.models import Note
# import json
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse_lazy('note_list')
        self.test_user = User.objects.create_user(username='testuser', password='pass@123', email='test@test.com')
        self.test_user_2 = User.objects.create_user(username='testuser2', password='2pass@123', email='test2@test.com')
        self.test_note = Note.objects.create(title = 'test note', body = 'slim', user = self.test_user)
        self.detail_url = reverse('note_detail', kwargs = {'pk': self.test_note.pk})
        self.new_note_url = reverse('note_new') # było reverse_lazy, robimy test
        self.delete_note_url = reverse('note_delete', kwargs = {'pk': self.test_note.pk})

    # TESTS LIST NOTE

    def test_note_list_user_not_logged_in_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 302)

    def test_note_list_user_logged_in_GET(self):
        self.client.login(username = self.test_user.username, password = 'pass@123')

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes_engine/note_list.html')

    # TESTS DETAIL NOTE

    def test_note_detail_user_not_logged_in(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 302)

    def test_note_detail_user_logged_in(self):
        self.client.login(username = self.test_user.username, password = 'pass@123')

        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes_engine/note_detail.html')

    def test_note_detail_wrong_user_logged_in(self):
        self.client.login(username = self.test_user_2.username , password = '2pass@123')

        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code , 403)

    # TESTS CREATE NOTE

    def test_add_new_note_user_not_logged_in_GET(self):
        response = self.client.get(self.new_note_url)

        self.assertEquals(response.status_code, 302)

    def test_add_new_note_user_not_logged_in_POST(self):
        response = self.client.post(self.new_note_url , {
            'title': 'test note 2' ,
            'body': 'slim2' ,
            'user': self.test_user_2
        })

        self.assertEquals(response.status_code, 302)

    def test_add_new_note_user_logged_in_POST(self):
        self.client.login(username = self.test_user_2.username , password = '2pass@123')
        response = self.client.post(self.new_note_url, {
            'title': 'test note 2',
            'body': 'slim2',
            'user': self.test_user_2
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Note.objects.last().title, 'test note 2')

    def test_add_new_note_user_logged_in_GET(self):
        self.client.login(username = self.test_user_2.username , password = '2pass@123')

        response = self.client.get(self.new_note_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response, 'notes_engine/note_new.html')

    # TESTS DELETE NOTE
    def test_delete_note_user_not_logged_in_GET(self):
        response = self.client.get(self.delete_note_url)

        self.assertEquals(response.status_code , 302)

    def test_delete_note_user_logged_in_GET(self):
        self.client.login(username = self.test_user.username , password = 'pass@123')

        response = self.client.get(self.delete_note_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response, 'notes_engine/note_delete.html')

    def test_delete_note_wrong_user_logged_in_GET(self):
        self.client.login(username = self.test_user_2.username , password = '2pass@123')

        response = self.client.get(self.delete_note_url)

        self.assertEquals(response.status_code , 403)

    def test_delete_note_user_not_logged_in_DELETE(self):
        response = self.client.delete(self.delete_note_url)

        self.assertEquals(response.status_code , 302)

    def test_delete_note_wrong_user_logged_in_DELETE(self):
        self.client.login(username = self.test_user_2.username , password = '2pass@123')

        response = self.client.delete(self.delete_note_url)

        self.assertEquals(response.status_code , 403)

    def test_delete_note_user_logged_in_DELETE(self):
        self.client.login(username = self.test_user.username , password = 'pass@123')
        note_count = Note.objects.count()
        response = self.client.delete(self.delete_note_url)

        self.assertEquals(response.status_code , 302)
        self.assertEquals(Note.objects.count() , note_count - 1)
        pass

    # TESTS UPDATE NOTE TO BE HERE
