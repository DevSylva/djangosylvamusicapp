# Generated by Django 3.1.2 on 2020-12-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('link', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
