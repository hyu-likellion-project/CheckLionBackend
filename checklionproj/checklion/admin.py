from django.contrib import admin
from .models import Team,Student,Status,Week,TeamPoint

# Register your models here.
admin.site.register(Team)
admin.site.register(Student)
admin.site.register(Status)
admin.site.register(Week)
admin.site.register(TeamPoint)