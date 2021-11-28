from django.db import models

class Orders (models.Model):

    number = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)

    kicthen = models.ForeignKey('kitchens.Kitchens', on_delete=models.PROTECT, related_name="orders")