# Generated by Django 3.2.6 on 2021-08-19 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20210819_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortenlink',
            old_name='shortened_slug',
            new_name='shorten_slug',
        ),
    ]