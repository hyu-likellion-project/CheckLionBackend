# Generated by Django 3.2 on 2021-05-10 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklion', '0002_teampoint_weekscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teampoint',
            old_name='AdditionalPoint',
            new_name='additionalPoint',
        ),
        migrations.RemoveField(
            model_name='teampoint',
            name='weekScore',
        ),
    ]
