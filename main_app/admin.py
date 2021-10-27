from django.contrib import admin

from .models import Photo, Todo, Note

admin.site.register(Todo)
admin.site.register(Note)
admin.site.register(Photo)
