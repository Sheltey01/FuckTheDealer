# Generated by Django 3.1.5 on 2021-03-14 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210314_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karte',
            name='usedByDealer',
        ),
    ]
