# Generated by Django 3.1.2 on 2020-12-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0014_auto_20201204_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
    ]