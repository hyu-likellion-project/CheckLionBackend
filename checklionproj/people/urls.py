from rest_framework.routers import DefaultRouter
from django.urls import path, include
from people import views

router = DefaultRouter()
router.register('team', views.TeamViewSet)
router.register('student', views.StudentViewSet)


urlpatterns = [
    path('', include(router.urls))
]