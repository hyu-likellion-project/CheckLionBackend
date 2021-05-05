from rest_framework import viewsets
from .models import Status,TeamPoint
from .serializers import StatusSerializer,TeamPointSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TeamPointViewSet(viewsets.ModelViewSet):
    queryset = TeamPoint.objects.all()
    serializer_class = TeamPointSerializer



