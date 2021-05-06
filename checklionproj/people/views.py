from rest_framework import viewsets
from .models import Team, Student
from .serializers import TeamSerializer, StudentSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('-totalScore')
    serializer_class = TeamSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        teamid = self.request.query_params.get("teamid", None)
        if teamid is not None:
            queryset = queryset.filter(team_id=teamid)
        return queryset


