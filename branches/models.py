from django.db import models


class Branches (models.Model):

    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=5)
    city = models.CharField(max_length=255)
    UF = models.CharField(max_length=2)
    cep = models.CharField(max_length=11)
