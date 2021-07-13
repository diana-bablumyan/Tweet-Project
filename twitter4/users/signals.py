from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_profile(instance, created, sender, **kwargs):
    if created:
        Profile.objects.create(user=instance, name="Name", age=0, profile_image="profile")


post_save.connect(create_profile, sender=User)
