# models.py in FeedbackApp
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.name
