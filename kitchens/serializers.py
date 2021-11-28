from rest_framework import serializers
from .models import Kitchens


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchens
        exclude = ['password']
