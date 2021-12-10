from rest_framework import serializers
from .models import Informations
from accounts.serializers import UserSerializer


class InformationsSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Informations
        fields = "__all__"
