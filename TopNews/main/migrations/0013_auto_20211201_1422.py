# Generated by Django 3.2.9 on 2021-12-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211201_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(null=True, upload_to='profiles'),
        ),
    ]