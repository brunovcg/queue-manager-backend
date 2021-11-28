from django.db import models
from django.contrib.auth.models import AbstractUser


def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)


class User (AbstractUser):

    image = models.ImageField(upload_to=upload_to)
    legal_id = models.CharField(max_length=14, unique=True)
