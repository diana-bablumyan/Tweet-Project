from django.db import models

# Create your models here.


class Email(models.Model):
    sender = models.EmailField()
    name = models.CharField(max_length=50)
    message = models.TextField()
    date_send = models.DateField(auto_now_add=True)
