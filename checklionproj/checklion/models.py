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

class Week(models.Model):
    weeknumber = models.IntegerField(default=0)
    info = models.CharField(max_length=30)

    def __str__(self):
        return str(self.weeknumber)

class Status(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # 학생을 지우면 스코어도 지워진다.
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
    assignment = models.BooleanField()
    attendance = models.BooleanField()
    lecture = models.BooleanField()

    def __str__(self):
        return str(self.id)

class TeamPoint(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
    AdditionalPoint = models.IntegerField(default=0)
    assignmentPass = models.IntegerField(default=0)
    attendancePass = models.IntegerField(default=0)
    lecturePass = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

