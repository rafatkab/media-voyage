# Generated by Django 4.2.4 on 2023-08-24 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0006_alter_movieratingslist_movie_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieRatingsList',
        ),
    ]
