# Generated by Django 3.1.2 on 2020-12-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0017_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
