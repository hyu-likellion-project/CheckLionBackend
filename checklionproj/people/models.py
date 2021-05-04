from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=30)
    totalScore = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 유저를 지우면 author도 지워진다
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)      # 팀을 삭제하면 null값으로 바뀜

    def __str__(self):
        return self.user.username