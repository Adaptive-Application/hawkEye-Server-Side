from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import trendingNewsSerializer
from .models import trendingNews


class trendinNewsApiView(APIView):

    def get(self, request):
        # user = request.user
        # if user.is_authenticated:
            tNews = trendingNews.objects.all()
            serializer = trendingNewsSerializer(tNews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response({"status": "authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)


