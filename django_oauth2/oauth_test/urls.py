from django.contrib import admin
from django.urls import path, include

from oauth_test.views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    path('address/', AddressList.as_view()),
    path('address/<pk>/', AddressList.as_view()),
    path('country/', CountryList.as_view()),
    path('country/<pk>/', CountryList.as_view()),
    path('city/', CityList.as_view()),
    path('city/<pk>/', CityList.as_view()),
]

