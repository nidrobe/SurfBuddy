from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

class CreateUserTests(TestCase):
    def setUp(self):
        self.client = APIClient() 
        self.factory = APIRequestFactory()

    # Simulate a POST request to the /api/create_user/ endpoint with JSON data.
    def test_create_user(self):
        url = reverse('create_user')  
    # Providing data for creating a user
        data = {
                "username": "testuser",
                "password": "testpassword",
            }
    
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check for success