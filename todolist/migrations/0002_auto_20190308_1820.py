# Generated by Django 2.1.7 on 2019-03-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='created_time',
            field=models.TimeField(default='12:20'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='due_time',
            field=models.TimeField(default='12:20'),
        ),
    ]