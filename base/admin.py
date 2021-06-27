from django.contrib import admin
from .models import contacts, user, posts

# Register your models here.

admin.site.register(contacts)
admin.site.register(posts)
admin.site.register(user)