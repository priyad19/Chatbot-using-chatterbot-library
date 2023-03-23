from django.db import models

class Conversation(models.Model):
    input_text = models.CharField(max_length=255)
    response_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
