# Generated by Django 4.1.6 on 2023-04-06 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, null=True)),
                ('status', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SearchCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=10)),
                ('subject_description', models.CharField(max_length=200)),
                ('catalog_number', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=400)),
                ('units', models.CharField(max_length=10)),
                ('class_number', models.IntegerField()),
                ('instructors', models.CharField(max_length=400)),
                ('days', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('classroom', models.CharField(max_length=100)),
                ('enrollment_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('stud_name', models.CharField(max_length=200)),
                ('comp_id', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=10)),
                ('subject_description', models.CharField(default='', max_length=200)),
                ('catalog_number', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=200)),
                ('topic', models.CharField(default='', max_length=400)),
                ('units', models.CharField(default='', max_length=10)),
                ('class_number', models.IntegerField(default=0)),
                ('instructors', models.CharField(default='', max_length=400)),
                ('days', models.CharField(default='', max_length=100)),
                ('start_time', models.CharField(default='', max_length=100)),
                ('end_time', models.CharField(default='', max_length=100)),
                ('classroom', models.CharField(default='', max_length=100)),
                ('enrollment_status', models.CharField(default='', max_length=10)),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduleadvisor.schedule')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduleadvisor.student'),
        ),
        migrations.CreateModel(
            name='CartCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=10)),
                ('subject_description', models.CharField(max_length=200)),
                ('catalog_number', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=400)),
                ('units', models.CharField(max_length=10)),
                ('class_number', models.IntegerField()),
                ('instructors', models.CharField(max_length=400)),
                ('days', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('classroom', models.CharField(max_length=100)),
                ('enrollment_status', models.CharField(max_length=10)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduleadvisor.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduleadvisor.student'),
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('adv_name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
