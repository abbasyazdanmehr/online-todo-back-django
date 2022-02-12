
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
    path('token/', obtain_auth_token, name='api-token'),
]
