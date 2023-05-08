# Generated by Django 4.1.7 on 2023-05-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scheduleadvisor", "0012_cartcourse_acad_career_descr_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartcourse",
            name="title",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="cartcourse",
            name="topic",
            field=models.CharField(default="", max_length=400),
        ),
        migrations.AlterField(
            model_name="searchcourse",
            name="title",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="searchcourse",
            name="topic",
            field=models.CharField(default="", max_length=400),
        ),
    ]
