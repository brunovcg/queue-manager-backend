from django.db import models
from accounts.models import User


def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)

class Kitchens (models.Model):

    code = models.CharField(max_length=255, unique=True)
    image = models.FileField(upload_to=upload_to, default="media/default.jpg", blank=True)
    label = models.CharField(max_length=255,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kitchens", blank=True, null=True)
    branch = models.ForeignKey('branches.Branches', on_delete=models.CASCADE, related_name="kitchens",blank=True)


