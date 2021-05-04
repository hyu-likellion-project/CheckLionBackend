from rest_framework.routers import DefaultRouter
from django.urls import path, include
from checklion import views

router = DefaultRouter()
router.register('status', views.StatusViewSet)



urlpatterns = [
    path('', include(router.urls))
]