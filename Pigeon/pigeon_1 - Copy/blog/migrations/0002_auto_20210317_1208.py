# Generated by Django 3.1.5 on 2021-03-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Music', 'Music'), ('Social', 'Social')], max_length=100),
        ),
    ]
