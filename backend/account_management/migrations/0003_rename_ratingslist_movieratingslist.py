# Generated by Django 4.2.4 on 2023-08-22 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0002_ratingslist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RatingsList',
            new_name='MovieRatingsList',
        ),
    ]
