from .models import Team, Student
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Student
        fields = ('id','user_name','team')