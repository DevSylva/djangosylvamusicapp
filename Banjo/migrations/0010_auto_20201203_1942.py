# Generated by Django 3.1.2 on 2020-12-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0009_contactinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
