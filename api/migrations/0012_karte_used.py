# Generated by Django 3.1.5 on 2021-03-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210314_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='karte',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
