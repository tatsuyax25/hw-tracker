from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo




# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def todos_index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', { 'todos': todos })

def todos_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/detail.html', {'todo' : todo})


class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'
    
class TodoUpdate(UpdateView):
    model = Todo
  # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'date']
    
class TodoDelete(DeleteView):
      model = Todo
      success_url = '/todos/'
