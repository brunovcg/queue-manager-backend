from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Branches
from .serializers import BranchesSerializer
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsSuperuser, IsSuperuserStaffCanGet

class BranchesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserStaffCanGet]
    

    def post(self, request):

        data = request.data

        try:
            branch = Branches.objects.get_or_create(**data)

        except IntegrityError:
            return Response({'message' : 'A branch with this name already exists'},status=status.HTTP_409_CONFLICT)

        serialized = BranchesSerializer(branch[0])      

        if not branch[1]:
            return Response({'message' : 'This branch already exists'},status=status.HTTP_409_CONFLICT)

        return Response(serialized.data,status=status.HTTP_201_CREATED)


    def get(self, request):

        branches = Branches.objects.all()
        serialized = BranchesSerializer(branches, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)


class BranchesDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuser]
    

    def patch(self,request, branch_id=""):

        branch = get_object_or_404(Branches, id=branch_id)
        serialized = BranchesSerializer(branch, request.data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)


    def get(self,request, branch_id=""):

        branch = get_object_or_404(Branches, id=branch_id)
        serialized = BranchesSerializer(branch)

        return Response(serialized.data, status=status.HTTP_200_OK)


    def delete(self,request, branch_id=""):

        branch = get_object_or_404(Branches, id=branch_id)
        branch.delete()

        return Response({'message' : f"Branch {branch_id} deleted"},status=status.HTTP_200_OK)