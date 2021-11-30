# Generated by Django 3.2.9 on 2021-11-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
