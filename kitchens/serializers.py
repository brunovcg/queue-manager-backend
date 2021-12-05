from rest_framework import serializers
from .models import Kitchens
from accounts.serializers import UserSerializer
from branches.serializers import BranchesSerializer
from orders.serializers import OrderNoKitchenSerializer


class KitchenSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    branch = BranchesSerializer()
    orders = OrderNoKitchenSerializer(many=True)

    class Meta:
        model = Kitchens
        fields = "__all__"


class KitchenUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kitchens
        fields = "__all__"
