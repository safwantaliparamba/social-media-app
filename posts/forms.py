from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created_at', 'author','likes','is_deleted']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author','likes','is_deleted']
