from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsStaff


class OrdersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def get(self, request):

        order = Orders.objects.all()
        serialized =  OrdersSerializer(order, many=True)

        return Response(serialized.data,status=status.HTTP_200_OK)


    def delete(self, request):

        orders = Orders.objects.all()

        if orders:
            orders.delete()
            return Response({"message" : "All Order has been deleted"},status=status.HTTP_200_OK)

        return Response({"message" : "There are no Orders to DELETE"},status=status.HTTP_200_OK)
