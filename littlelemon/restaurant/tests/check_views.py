from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer  # Replace with your actual serializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up test instances of the Menu model
        self.menu1 = Menu.objects.create(name='Dish1', price=10.99, category='Main Course')
        self.menu2 = Menu.objects.create(name='Dish2', price=8.99, category='Appetizer')
        # Add more instances as needed

    def test_getall(self):
        # Retrieve all Menu objects
        url = reverse('menu-list')  # Replace 'menu-list' with your actual URL name
        client = APIClient()
        response = client.get(url)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data in the response matches the expected serialized data
        self.assertEqual(response.data, serialized_data)
