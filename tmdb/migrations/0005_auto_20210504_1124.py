# Generated by Django 3.2 on 2021-05-04 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0004_auto_20210427_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='age',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
    ]
