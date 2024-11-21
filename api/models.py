# api/models.py
from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django.conf import settings

class Session(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,  # Ensures user's sessions are deleted with the user
        related_name='sessions'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} for user {self.user.username} started at {self.created_at}"

class Message(models.Model):
    # Fields
    session = models.ForeignKey(Session, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    from_user = models.BooleanField(default=True)  # True if from user, False if from system (LangChain)

    def __str__(self):
        return f"Message from {'User' if self.from_user else 'System'} at {self.timestamp}: {self.text[:50]}"
