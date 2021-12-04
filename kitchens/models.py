from django.db import models
from accounts.models import User


def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)

class Kitchens (models.Model):

    code = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=upload_to, default="default.jpg")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kitchens")
    branch = models.ForeignKey('branches.Branches', on_delete=models.CASCADE, related_name="kitchens")


