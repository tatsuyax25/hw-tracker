from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateTimeField('due date')



    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse('todos_detail', kwargs={'todo_id': self.id})