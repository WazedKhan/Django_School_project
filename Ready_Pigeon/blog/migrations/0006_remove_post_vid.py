# Generated by Django 3.1.5 on 2021-03-23 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210323_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='vid',
        ),
    ]