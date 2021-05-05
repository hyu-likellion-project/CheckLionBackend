from .models import Status,TeamPoint
from rest_framework import serializers

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TeamPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPoint
        fields = '__all__'
