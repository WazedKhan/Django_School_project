# Generated by Django 3.1.5 on 2021-03-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='pro.jpg', upload_to='profile_pics'),
        ),
    ]
