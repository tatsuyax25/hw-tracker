from django.contrib import admin

from .models import Todo, Note

admin.site.register(Todo)
admin.site.register(Note)
