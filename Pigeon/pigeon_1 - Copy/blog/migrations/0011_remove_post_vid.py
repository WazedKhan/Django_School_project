# Generated by Django 3.1.5 on 2021-03-24 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210323_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='vid',
        ),
    ]
