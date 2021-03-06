from rest_framework import serializers
from branches.models import Branches

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = "__all__"
