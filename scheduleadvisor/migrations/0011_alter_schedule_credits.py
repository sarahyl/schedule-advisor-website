# Generated by Django 4.1.6 on 2023-05-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleadvisor', '0010_schedule_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='credits',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
    ]
