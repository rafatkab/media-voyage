# Generated by Django 4.2.4 on 2023-08-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
