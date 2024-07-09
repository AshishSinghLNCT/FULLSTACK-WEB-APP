from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Interest(models.Model):
    sender = models.ForeignKey(User, related_name='sent_interests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_interests', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



