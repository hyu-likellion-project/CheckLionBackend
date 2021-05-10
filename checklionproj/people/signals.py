from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Team
from checklion.models import TeamPoint

@receiver(post_save, sender=TeamPoint)
def teampoint_post_save(sender, **kwargs):
    team=kwargs['instance'].team
    team.totalScore += kwargs['instance'].weekScore
    team.save()