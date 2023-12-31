# Generated by Django 4.2.4 on 2023-08-31 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0010_movieratingslist_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
