from django import forms
from rest_framework import serializers

from Blog.models import Blog
from allauth.account.views import LoginView

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtag = forms.CharField()
    image = forms.ImageField()

class CommentForm(forms.Form):
     text = forms.CharField()


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'image',
            'title',
            'description',
            'hashtag'

        ]