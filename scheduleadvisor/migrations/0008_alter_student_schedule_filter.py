# Generated by Django 4.1.6 on 2023-04-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleadvisor', '0007_student_schedule_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='schedule_filter',
            field=models.CharField(default='All', max_length=100),
        ),
    ]
