# Generated by Django 3.1.5 on 2021-03-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210317_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vid',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]