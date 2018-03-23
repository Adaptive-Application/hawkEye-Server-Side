from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        print(request.user.auth_token)
        request.user.auth_token.delete()
        return Response({'status':'logged-out'},status=status.HTTP_200_OK)
