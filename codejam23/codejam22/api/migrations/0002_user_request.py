# Generated by Django 4.0 on 2022-11-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='request',
            field=models.ManyToManyField(blank=True, null=True, to='api.User'),
        ),
    ]
