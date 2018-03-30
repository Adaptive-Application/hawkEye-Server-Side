from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('update/preference/api', views.PreferenceView.as_view(), name='preference'),
    path('create/preference/api', views.CreatePreferenceView.as_view(), name='preference'),
    path('update/subpreference/api', views.SubPreferenceView.as_view(), name='subpreference'),
    path('create/subpreference/api', views.CreateSubPreferenceView.as_view(), name='subpreference'),
        ]