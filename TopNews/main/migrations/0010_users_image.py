# Generated by Django 3.2.9 on 2021-11-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
