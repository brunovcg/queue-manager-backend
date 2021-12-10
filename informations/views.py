from rest_framework.views import APIView
from rest_framework import status
from accounts.models import User
from .models  import Informations
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import InformationsSerializer
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import SuperuserGetForAll, IsSuperuser


class InformationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserGetForAll]

    def get(self,request):
        messages = Informations.objects.all()
        serialized = InformationsSerializer(messages, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self,request):

        user = request.user
        message  = Informations.objects.get_or_create(**request.data, user = user)

        if not message[1]:
            return Response({"message" : "This message already exists"},status=status.HTTP_409_CONFLICT)

        serialized = InformationsSerializer(message[0])

        return Response(serialized.data, status=status.HTTP_200_OK)
        

class InformationsDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuser]

    def patch(self,request, message_id=""):

        message = get_object_or_404(Informations, id = message_id)

        serialized = InformationsSerializer(message, request.data, partial=True)
        
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)

        return Response({'message' : "some error occured"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, message_id=""):
        
        message = get_object_or_404(Informations, id=message_id )
        message.delete()

        return Response({'message' : f"Message {message_id} deleted"},status=status.HTTP_200_OK)

