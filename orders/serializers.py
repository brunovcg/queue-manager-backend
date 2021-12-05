from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class OrderNoKitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        exclude=["kitchen"]
