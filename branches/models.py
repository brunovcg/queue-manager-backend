from django.db import models


class Branches (models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=11)
