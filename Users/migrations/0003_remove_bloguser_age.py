# Generated by Django 3.2.6 on 2021-09-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_bloguser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='age',
        ),
    ]