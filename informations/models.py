from django.db import models
from accounts.models import User

class Informations (models.Model):

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="informations")
 