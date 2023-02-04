from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Note(models.Model):

    title = models.CharField(max_length = 40)
    body = models.TextField(max_length = 5000)
    created = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs = {'pk': self.pk})
