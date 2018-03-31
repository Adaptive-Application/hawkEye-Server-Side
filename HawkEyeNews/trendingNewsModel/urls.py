from django.urls import path
from . import views

urlpatterns = [
    path('api', views.trendinNewsApiView.as_view(), name='trendingNews'),
]
