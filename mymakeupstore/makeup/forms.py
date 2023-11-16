# En makeup/forms.py

from django import forms
from .models import Blog, Profile

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'date', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'website_link', 'image']
