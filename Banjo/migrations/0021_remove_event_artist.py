# Generated by Django 3.1.2 on 2020-12-04 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0020_auto_20201204_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='artist',
        ),
    ]