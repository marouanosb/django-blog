from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This receiver triggers when a User is created, it will create a profile object with the User instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #kwargs = any additional args
    if created:
        Profile.objects.create(user=instance)

# Same for when a user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
