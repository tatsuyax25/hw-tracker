from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('todos/', views.todos_index, name='index'),
    path('todos/<int:todo_id>/', views.todos_detail, name='todos_detail'),
    path('todos/create/', views.TodoCreate.as_view(), name='todos_create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
]