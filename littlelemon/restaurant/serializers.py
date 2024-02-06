from django.contrib.auth.models import User
from .models import MenuItem, Booking
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory'] 

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        #fields = ['id', 'name', 'no_of_guests', 'booking_date']
        fields = '__all__'
 