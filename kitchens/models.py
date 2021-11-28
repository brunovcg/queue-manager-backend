from django.db import models
from accounts.models import User


class Kitchens (models.Model):

    code = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="kitchens")
    branch = models.ForeignKey('branches.Branches', on_delete=models.PROTECT, related_name="kitchens")


