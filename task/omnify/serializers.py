from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User=get_user_model()

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=FitnessClass
        fields='__all__'
    

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields='__all__'
        