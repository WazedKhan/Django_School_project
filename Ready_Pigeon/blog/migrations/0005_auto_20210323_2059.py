# Generated by Django 3.1.5 on 2021-03-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210323_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.png', upload_to='Photos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='vid',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
