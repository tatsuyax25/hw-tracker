from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from .models import Todo, Note, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'frogcollector'

# Define the home view
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def todos_index(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {'todos': todos})


@login_required
def todos_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/detail.html', {'todo': todo})


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['todo', 'description', 'date', 'time']

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(self.request, "REQUEST CHECK")
        return super().form_valid(form)


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'date', 'time']


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/todos/'

@login_required
def notes_index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', { 'notes': notes })
@login_required
def notes_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/detail.html', { 'note': note })

class NoteCreate(LoginRequiredMixin, CreateView):
  model = Note
  fields = ['note', 'content']

  def form_valid(self, form):
        # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
  # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['content']

class NoteDelete(LoginRequiredMixin, DeleteView):
  model = Note
  success_url = '/notes/'

def add_photo(request, todo_id):
        # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, todo_id=todo_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('todos_detail', todo_id=todo_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


  