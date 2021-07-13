from django.db import models
from django.contrib.auth.models import User


class NewTweet(models.Model):

    tweet = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tweet


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tweet = models.ForeignKey(NewTweet, on_delete=models.CASCADE, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(NewTweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
