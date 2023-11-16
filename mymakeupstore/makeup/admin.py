from django.contrib import admin


# En makeup/admin.py

from django.contrib import admin
from .models import Blog, Profile

admin.site.register(Blog)
admin.site.register(Profile)
