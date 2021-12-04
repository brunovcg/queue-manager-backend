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
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 


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
                legal_id = request.data["legal_id"],
            )
        except IntegrityError:
            return Response({"user already exists"},status=status.HTTP_409_CONFLICT)

        serialized = UserSerializer(new_user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class UserView(APIView):

    def get(self,request):

        users = User.objects.all()

        serialized = UserSerializer(users, many=True)

        return Response(serialized.data,status=status.HTTP_200_OK)


class UserDetailView(APIView):

    def get(self,request, user_id=""):

        user = get_object_or_404(User, id=user_id)
        serialized = UserSerializer(user)

        return Response(serialized.data,status=status.HTTP_200_OK)


    def delete(self,request, user_id=""):

        user = get_object_or_404(User, id=user_id)
        user.delete()

        return Response({'message' : f"user {user_id} deleted"},status=status.HTTP_200_OK)


    def patch(self,request, user_id=""):

        user = get_object_or_404(User, id=user_id)

        serialized = UserSerializer(user, request.data, partial=True)

        fields = ["username", "email", "password", "is_superuser", "is_staff", "legal_id", 'password']
        wrong_fields = []

        for item in request.data:
            wrong_fields = []

            if item == 'password':
                return Response({'message' : 'this end-point does not update PASSWORD'} , status=status.HTTP_400_BAD_REQUEST)

            if item not in fields:
                wrong_fields.append(item)

        if len(wrong_fields) > 0:

            return Response({'message' : {'wrong_fields' : wrong_fields}} , status=status.HTTP_400_BAD_REQUEST)
        
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)

        return Response({'message' : 'wrong parrameters'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):

    def patch(self,request, user_id=""):
        
        user = get_object_or_404(User, id=user_id)

        user.set_password(request.data['password'])

        user.save()

        return Response({"message" : "Password Reseted"}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    def patch(self,request, user_id=""):

        user = get_object_or_404(User, id=user_id)

        if not user.check_password(request.data['old_password']):
            return Response({"message" : "old Password is invalid"}, status=status.HTTP_401_UNAUTHORIZED)

        user.set_password(request.data['new_password'])

        user.save()

        return Response({"message" : "Password Updated"}, status=status.HTTP_200_OK)
