# Generated by Django 3.2 on 2021-05-04 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0008_alter_show_premier_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='show',
        ),
        migrations.DeleteModel(
            name='Show',
        ),
    ]
