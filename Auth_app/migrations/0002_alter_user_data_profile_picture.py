# Generated by Django 5.1.6 on 2025-02-25 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='profile_picture',
            field=models.ImageField(upload_to='mysite/static/profile_pictures/'),
        ),
    ]
