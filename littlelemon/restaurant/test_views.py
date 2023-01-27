from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
from django.contrib.auth.models import User
user = User.objects.create_user(username='testuser', password='testpassword')

class MenuViewTest(TestCase):
    def setUp(self):
        # create test instances of the Menu model
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Test Menu 1', price=5.00, inventory=2)
        self.menu2 = Menu.objects.create(title='Test Menu 2', price=15.00, inventory=3)
        self.menu3 = Menu.objects.create(title='Test Menu 3', price=25.00, inventory=4)

        from django.contrib.auth.models import User
        user = User.objects.create_user(username='testuser', password='testpassword')

    def test_getall(self):
        # retrieve all the Menu objects added for the test purpose
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')
        self.assertEqual(response.status_code, 200)

        # serialize the data
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)