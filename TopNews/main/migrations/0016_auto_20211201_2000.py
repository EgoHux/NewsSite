# Generated by Django 3.2.9 on 2021-12-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211201_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='login',
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.TextField(),
        ),
    ]
