from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OrdersView(APIView):

    def get(self, request):

        return Response("teste",status=status.HTTP_201_CREATED)


    def delete(self, request):
        return Response("teste",status=status.HTTP_204_NO_CONTENT)


