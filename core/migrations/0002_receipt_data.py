# Generated by Django 2.1 on 2018-12-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
