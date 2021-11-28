from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.models import User
from rest_framework import status
from django.db import IntegrityError
from .serializers import UserSerializer
from kitchens.models import Kitchens
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .serializers import LoginSerializer


class LoginView(APIView):
    def post(self, request):
    
        username= request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
    
        if user:         
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})

  
        return Response({"error": "Wrong email or password"}, status=status.HTTP_401_UNAUTHORIZED)


class SignupView(APIView):
    def post(self, request):
        
        try:
            new_user =  User.objects.create_user(
                username = request.data["username"],
                email = request.data["email"],
                password = request.data["password"],
                is_superuser = request.data["is_superuser"],
                is_staff = request.data["is_staff"],
                image = None,
                legal_id = request.data["legal_id"],
            )
        except IntegrityError:
            return Response({"user already exists"},status=status.HTTP_409_CONFLICT)

        serialized = UserSerializer(new_user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class ImagesView(APIView):
    parser_classes=[MultiPartParser, FormParser]


    def post(self, request, format=None):

        serializer = UserSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):

        all_data = [],

        kitchen = Kitchens.objects.all()

        all_data = [{
            'kitchen_id': item.id,
            'user_id': kitchen.user.id,
            'image': kitchen.user.image
            } for item in kitchen]

        return Response(all_data, status=status.status.HTTP_200_OK)


        
class ImagesDetailView(APIView):
    parser_classes=[MultiPartParser, FormParser]

    def patch(self, request, user_id="", format=None):

        user = get_object_or_404(User,id=user_id)

        fields = ['username', 'password', 'email', 'is_staff', 'is_superuser', 'legal_id', 'image']

        for item in fields:
            if request.data[item]:

                key = item
                
                exec("%s = %d" % (key, request.data[item]))

                user.item = request.data[item]

                user.save()

        serialized = UserSerializer(user)

        return Response(serialized.data, status=status.HTTP_200_OK)
        