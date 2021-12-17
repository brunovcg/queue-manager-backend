from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsStaff
from django.shortcuts import get_object_or_404
from branches.models import Branches
from kitchens.models import Kitchens

class OrdersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def get(self, request):

        order = Orders.objects.all()
        serialized =  OrdersSerializer(order, many=True)

        return Response(serialized.data,status=status.HTTP_200_OK)

class OrdersBranchView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def delete(self, request, branch_id=""):

        branch = get_object_or_404(Branches, id= branch_id)

        kitchens_list = Kitchens.objects.filter(branch=branch)

        orders = Orders.objects.filter(kitchen__in=kitchens_list  ) 

        if orders:
            orders.delete()
            return Response({"message" : f"All Orders from Branch {branch.name} has been deleted"},status=status.HTTP_200_OK)

        return Response({"message" : "There are no Orders to DELETE"},status=status.HTTP_200_OK)
