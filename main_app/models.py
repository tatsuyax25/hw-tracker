from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=100)
    # category = models. (should have choices)
    description = models.TextField(max_length=250)
    date = models.CharField('due date', max_length=30)
    time = models.CharField(max_length=12)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse('todos_detail', kwargs={'todo_id': self.id})


class Note(models.Model):
    note = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return self.note

    def get_absolute_url(self):
        return reverse('notes_detail', kwargs={'note_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for todo_id: {self.todo_id} @{self.url}"
        
class Meta:
    ordering = ['-date']