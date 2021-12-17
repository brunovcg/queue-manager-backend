from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from branches.models import Branches
from kitchens.models import Kitchens
from django.shortcuts import get_object_or_404
from .serializers import KitchenSerializer, KitchenUpdateSerializer
from orders.serializers import OrdersSerializer
from orders.models import Orders
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsUserOrSuperuser, IsSuperuserStaffCanGet
from rest_framework.parsers import MultiPartParser, FormParser


class KitchensView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserStaffCanGet]
    # parser_classes = [ MultiPartParser, FormParser]


    def post(self,request):

        serialized =  KitchenUpdateSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return  Response(serialized.data, status=status.HTTP_201_CREATED)

        else:   
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        
        kitchens = Kitchens.objects.all()

        serialized = KitchenSerializer(kitchens, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)



class KitchensDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOrSuperuser, IsAuthenticated]

    def patch(self,request, kitchen_id=""):
        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        serialized = KitchenUpdateSerializer(kitchen, request.data, partial=True)

        if not request.user.is_superuser:
            return Response({"message" : "Superuser authorization is needed"}, status=status.HTTP_401_UNAUTHORIZED)
  
        try:
            user =  int(request.data['user'])
            try:
               get_object_or_404(User, id=user)
            except Exception:
                return Response({"message" : "This user does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except:
            ...

        try:
            branch =  int(request.data['branch'])
            try:
               get_object_or_404(Branches, id=branch)
            except Exception:
                return Response({"message" : "This branch does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except:
            ...

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)


    def get(self,request, kitchen_id=""):

        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        user_logged = request.user

        if not user_logged.is_superuser and kitchen.user.id != user_logged:
            return Response({"message": "User can only GET it's own kitchen's orders"}, status=status.HTTP_401_UNAUTHORIZED)

        serialized = KitchenSerializer(kitchen)

        return Response(serialized.data, status=status.HTTP_200_OK)


    def delete(self,request, kitchen_id=""):

        if not request.user.is_superuser:
            return Response({"message" : "Superuser authorization is needed"}, status=status.HTTP_401_UNAUTHORIZED)

        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        kitchen.delete()
        return Response({'message' : f"Kitchen {kitchen_id} deleted"},status=status.HTTP_200_OK)



class KitchensDetailOrdersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOrSuperuser, IsAuthenticated]


    def get(self,request, kitchen_id=""):

        kitchen = get_object_or_404(Kitchens,id = kitchen_id )

        user_logged = request.user

        if not user_logged.is_superuser and kitchen.user.id != user_logged.id:
            return Response({"message": "User can only GET it's own kitchen's orders"}, status=status.HTTP_401_UNAUTHORIZED)


        orders = Orders.objects.filter(kitchen = kitchen_id)

        serialized = OrdersSerializer(orders, many=True)

        return Response(serialized.data,status=status.HTTP_200_OK)     


    def post(self,request, kitchen_id=""):

        kitchen = get_object_or_404(Kitchens, id=kitchen_id )
        user_logged = request.user

        if not user_logged.is_superuser and kitchen.user.id != user_logged:
            return Response({"message": "User can only POST it's own kitchen's orders"}, status=status.HTTP_401_UNAUTHORIZED)

        order = Orders.objects.get_or_create(number=request.data['number'], kitchen=kitchen)

        if not order[1]:
            return Response({"message" : "This order already exists"},status=status.HTTP_409_CONFLICT)

        serialized = OrdersSerializer(order[0])

        return Response(serialized.data,status=status.HTTP_201_CREATED)


    def delete(self, request, kitchen_id=""):

        kitchen = get_object_or_404(Kitchens, id=kitchen_id )
        user_logged = request.user

        if not user_logged.is_superuser and kitchen.user.id != user_logged:
            return Response({"message": "User can only POST it owns kitchen`s orders"}, status=status.HTTP_401_UNAUTHORIZED)      

        orders = Orders.objects.filter(kitchen = kitchen_id)
        
        if orders:
            orders.delete()
            return Response({"message": f"You have deleted all this Kitchen`s {kitchen.name} Orders"}, status=status.HTTP_200_OK)

        return Response({"message": "No Order to delete for this Kitchen"}, status=status.HTTP_200_OK)


class KitchensDetailOrdersDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOrSuperuser, IsAuthenticated]

    def delete(self,request, kitchen_id="", order_id=""):

        user_logged = request.user
        kitchen = get_object_or_404(Kitchens, id=kitchen_id)
        
        if not user_logged.is_superuser and kitchen.user.id != user_logged:
            return Response({"message": "User can only delete it owns kitchen orders"}, status=status.HTTP_401_UNAUTHORIZED)

        order = get_object_or_404(Orders, id= order_id)

        if order.__dict__['kitchen_id'] != kitchen_id:
            return Response({"message": "User can only delete it owns kitchen orders"}, status=status.HTTP_401_UNAUTHORIZED)

        order.delete()      
    
        return Response(f"Order {order.number} has been deleted",status=status.HTTP_200_OK)
