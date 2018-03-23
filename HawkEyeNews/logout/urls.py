from django.urls import path
from . import views

urlpatterns = [
    path('api', views.Logout.as_view(), name='logout'),
    ]