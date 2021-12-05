from django.db import models

class Orders (models.Model):

    number = models.CharField(max_length=6)
    creation_date = models.DateField(auto_now_add=True)

    kitchen = models.ForeignKey('kitchens.Kitchens', on_delete=models.CASCADE, related_name="orders")
    