from django.contrib import admin
from django.urls import path, include

from oauth_test.views import UserList, UserDetails, GroupList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('oauth_test.urls')),
]

