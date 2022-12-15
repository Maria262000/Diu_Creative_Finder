# Generated by Django 4.1 on 2022-08-19 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListofInterests',
            fields=[
                ('interest', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_picture', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('interest1', models.CharField(max_length=30)),
                ('interest2', models.CharField(max_length=30)),
                ('interest3', models.CharField(max_length=30)),
                ('interest1_link', models.CharField(max_length=100)),
                ('interest2_link', models.CharField(max_length=100)),
                ('interest3_link', models.CharField(max_length=100)),
                ('interest1_bio', models.CharField(max_length=140)),
                ('interest2_bio', models.CharField(max_length=140)),
                ('interest3_bio', models.CharField(max_length=140)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]