from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PreferenceSerializer, SubPreferenceSerializer
from . import models


# Create your views here.


class PreferenceView(APIView):

    def put(self, request):
        user = request.user
        if user.is_authenticated:

            serializer = PreferenceSerializer.update(self, instance=models.userPreference,
                                                     validated_data={"username": user, "data": request.data})

            print(serializer)
            if 0 not in serializer:
                return Response({'status': 'preference updated'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'updation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:

            return Response({'status': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


class CreatePreferenceView(APIView):

    def post(self, request):
        user = request.user
        if user.is_authenticated:

            serializer = PreferenceSerializer.create(self, validated_data={"username": user, "data": request.data})

            if 0 not in serializer:
                return Response({'status': 'preference created'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:

            return Response({'status': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


class SubPreferenceView(APIView):

    def put(self, request):
        user = request.user
        if user.is_authenticated:

            serializer = SubPreferenceSerializer.update(self, instance=models.userSubPreference,
                                                     validated_data={"username": user, "data": request.data})

            print(serializer)
            if 0 not in serializer:
                return Response({'status': 'preference updated'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'updation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:

            return Response({'status': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


class CreateSubPreferenceView(APIView):

    def post(self, request):
        user = request.user
        if user.is_authenticated:

            serializer = SubPreferenceSerializer.create(self, validated_data={"username": user, "data": request.data})

            if 0 not in serializer:
                return Response({'status': 'preference created'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:

            return Response({'status': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
