from django.contrib.auth.models import User, Group
from django.shortcuts import render
from oauth_test.models import Address, Country, City
from rest_framework.response import Response


# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions

from oauth_test.serializers import *


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AddressList(generics.ListCreateAPIView):
    
       # Address Get List class. aşşagıdakilerde benzeridir.
    
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CountryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request):
        get_city = []
        for city in self.get_queryset():
            data = {
                "id": city.id,
                "name": city.name,
                "county": city.country.name                  #country name ler numaraya göre degil de yazı olarak gelsin diye""""
            }
            get_city.append(data)
        return Response(get_city)
