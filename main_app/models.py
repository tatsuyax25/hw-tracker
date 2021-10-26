from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateTimeField('due date')

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse('todos_detail', kwargs={'todo_id': self.id})

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
    ordering = ['-date']