# api/signals.py

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Signal to automatically create an authentication token whenever a new user is created.
    """
    if created:
        Token.objects.create(user=instance)
