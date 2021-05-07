from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static
from checklion import urls
from people import urls
from rest_auth import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('people.urls')),
    path('check/', include('checklion.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
