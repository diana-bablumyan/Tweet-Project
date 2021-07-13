from django.contrib import admin
from .models import NewTweet, Comment, Like

# Register your models here.

admin.site.register(NewTweet)
admin.site.register(Comment)
admin.site.register(Like)
