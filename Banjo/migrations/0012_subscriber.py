# Generated by Django 3.1.2 on 2020-12-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0011_event_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
