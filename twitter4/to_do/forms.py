from django.forms import ModelForm
from django import forms
from .models import NewTweet, Comment


class TweetForm(ModelForm):
    class Meta:
        model = NewTweet
        fields = ['tweet']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['date_create']

