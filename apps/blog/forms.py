from django.forms import ModelForm
from django import forms
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail']


class CommentForm(ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))

    class Meta:
        model = Comment
        fields = ('content',)
