from rest_framework import viewsets
from .models import Status,TeamPoint,Week
from .serializers import StatusSerializer,TeamPointSerializer,WeekSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        studentid = self.request.query_params.get("studentid", None)
        week = self.request.query_params.get("week", None)
        if studentid is not None and week is not None:
            queryset = queryset.filter(student=studentid)
            queryset = queryset.filter(week=week)
        return queryset

class TeamPointViewSet(viewsets.ModelViewSet):
    queryset = TeamPoint.objects.all()
    serializer_class = TeamPointSerializer

class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer



