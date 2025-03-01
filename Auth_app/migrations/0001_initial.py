# Generated by Django 5.1.6 on 2025-02-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('user_type', models.CharField(choices=[('doctor', 'Doctor'), ('patient', 'Patient')], max_length=7)),
            ],
        ),
    ]
