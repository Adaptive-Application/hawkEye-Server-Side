from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.


class PreferenceView(APIView):

    def post(self):
        print("hello")