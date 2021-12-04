from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from branches.models import Branches
from django.db import IntegrityError
from kitchens.models import Kitchens
from django.shortcuts import get_object_or_404
from .serializers import KitchenSerializer, KitchenUpdateSerializer


class KitchensView(APIView):

    def post(self,request):

        serializer = KitchenSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def get(self,request):

        branches = Kitchens.objects.all()
        serialized = KitchenSerializer(branches, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class KitchensDetailView(APIView):
    def patch(self,request, kitchen_id=""):
        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        serialized = KitchenUpdateSerializer(kitchen, request.data, partial=True)
  

        try:
            user =  int(request.data['user'])
            try:
               get_object_or_404(User, id=user)
            except Exception:
                return Response({"message" : "this user does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except:
            ...

        try:
            branch =  int(request.data['branch'])
            try:
               get_object_or_404(Branches, id=branch)
            except Exception:
                return Response({"message" : "this branch does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except:
            ...


        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)


    def get(self,request, kitchen_id=""):

        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        serialized = KitchenSerializer(kitchen)

        return Response(serialized.data, status=status.HTTP_200_OK)


    def delete(self,request, kitchen_id=""):

        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        kitchen.delete()
        return Response({'message' : f"Kitchen {kitchen_id} deleted"},status=status.HTTP_200_OK)



class KitchensDetailOrdersView(APIView):

    def get(self,request, kitchen_id=""):


        return Response("teste",status=status.HTTP_200_OK)


    def post(self,request, kitchen_id=""):


        return Response("teste",status=status.HTTP_200_OK)


class KitchensDetailOrdersDetailView(APIView):


    def delete(self,request, kitchen_id="", order_id=""):

        


        return Response("teste",status=status.HTTP_204_NO_CONTENT)
