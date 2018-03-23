from django.urls import reverse
from rest_framework.test import APITestCase

class AuthTest(APITestCase):
    def setUp(self):

        # URL for creating an account.
        self.create_url = reverse('signin')
    def authUser(self):
        data = {
            "username": "agrahr",
            "password": "qwertyuiop"
        }

        response = self.client.login(data)
        print(response)
