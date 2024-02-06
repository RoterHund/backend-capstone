from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = MenuItem.objects.create(title='PastaDish1', price=13.50, inventory=20)
        self.menu2 = MenuItem.objects.create(title='PastaDish2', price=14.50, inventory=10)


    def test_getall(self):
        url = reverse('menu-items')  
        response = self.client.get(url)
        serialized_data = MenuItemSerializer(MenuItem.objects.all(), many=True).data
        self.assertEqual(response.data, serialized_data)
