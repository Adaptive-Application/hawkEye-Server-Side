from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

class UserAuth(APIView):

    def post(self, request, format='json'):
        data = request.data
        print(data)
        user = authenticate(username = data['username'], password = data['password'])
        if user is not None:
            login(request, user)

            token = Token.objects.create(user=user)
            return Response({'status': 'Authentication Successful', 'token':token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Authentication fail'}, status=status.HTTP_401_UNAUTHORIZED)


