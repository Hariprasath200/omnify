from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from .pagination import *
from .models import *
from .serializers import *

class FitnessclassView(APIView):
    #After Completly done integration with frontend then want to update to Isauthenticated in Below line
    permission_classes=[AllowAny] 
    pagination_classes=Custompagination

    def get(self,request):
        #Here its Fetching all data 
        data=FitnessClass.objects.all()
        paginator=self.pagination_classes()
        page=paginator.paginate_queryset(data,request)
        serializer=FitnessClassSerializer(page,many=True,context={'request':request})
        if serializer:
            return paginator.get_paginated_response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_200_OK)

class BookingAccept(APIView):
     #After Completly done integration with frontend then want to update to Isauthenticated in Below line
    permission_classes=[AllowAny]
    def post(self,request):
        #Data want to send in Object format from react 
        data=request.data.copy()
        try:
            class_id=request.data.get('fitness_class_id')
            slot=FitnessClass.objects.get(id=class_id)
            if slot.available_slots>0:
                serializer=BookingSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    slot.available_slots-=1
                    slot.save()
                    return Response({"res":'Booking Done Successfully'},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error":"Slots Not Available"},status=status.HTTP_404_NOT_FOUND)
        except FitnessClass.DoesNotExist:
            return Response({"error":"Fitness Class Not Found"},status=status.HTTP_404_NOT_FOUND)

class AllBookingsView(APIView):#According to email it will fetch the data
    permission_classes=[AllowAny]
    pagination_class=Custompagination
    def get(self,request):
        user=request.user.email
        # It is Possible to fetch data using email input or else current authenticated user 
        # email=request.query_params.get('email')
        # bookings=Request.objects.filter(email=email)
        
        try:
            bookings=Request.objects.filter(email=user)#Fetching Data According To Current logged in User email
            if bookings.exists():
                paginator=self.pagination_class()
                page=paginator.paginate_queryset(bookings,request)
                serializer=BookingSerializer(page,many=True,context={'request':request})
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response({"errors":"Data Not Found"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':f'{e}'},status=status.HTTP_400_BAD_REQUEST)