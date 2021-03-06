from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = User.objects.create_user('testuser','test@example.com', 'testpassword')
        self.test_user.first_name = "amit"
        self.test_user.first_name = "prasad"
        # URL for creating an account.
        self.create_url = reverse('signup')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'first_name': 'ashish',
            'last_name': 'lochan',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url , data, format='json')
        print(response.data)
        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_no_password(self):
        data = {
            'username': 'foobar',
            'first_name': 'rahul',
            'last_name': 'agrahari',
            'email': 'foobarbaz@example.com',
            'password': ''
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user1(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'first_name': 'Xu',
            'last_name': 'Zeng',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url, data, format='json')
        user = User.objects.latest('id')
        print(response.data)
        token = Token.objects.get(user=user)

        self.assertEqual(response.data['token'], token.key)