# Generated by Django 3.1.2 on 2020-12-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0015_auto_20201204_1017'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
