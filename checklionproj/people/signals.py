from django.db.models.signals import post_save,pre_save, post_delete
from django.dispatch import receiver
from .models import Team
from checklion.models import TeamPoint

@receiver(pre_save, sender=TeamPoint)
def teampoint_pre_save(sender, **kwargs):
    teampointID = kwargs['instance'].pk
    team=kwargs['instance'].team
    try:
        pre_teampoint = TeamPoint.objects.get(pk=teampointID)
        pre_weekScore = pre_teampoint.additionalPoint + pre_teampoint.attendancePass + pre_teampoint.lecturePass + pre_teampoint.assignmentPass
        team.totalScore -= pre_weekScore
        team.save()
    except:
        pass

@receiver(post_save, sender=TeamPoint)
def teampoint_post_save(sender, **kwargs):
    team=kwargs['instance'].team
    weekScore = kwargs['instance'].additionalPoint + kwargs['instance'].attendancePass + kwargs['instance'].lecturePass + kwargs['instance'].assignmentPass
    team.totalScore += weekScore
    team.save()

@receiver(post_delete, sender=TeamPoint)
def teampoint_post_delete(sender, **kwargs):
    team=kwargs['instance'].team
    weekScore = kwargs['instance'].additionalPoint + kwargs['instance'].attendancePass + kwargs['instance'].lecturePass + kwargs['instance'].assignmentPass
    team.totalScore -= weekScore
    team.save()
