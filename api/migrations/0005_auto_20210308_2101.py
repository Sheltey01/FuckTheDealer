# Generated by Django 3.1.5 on 2021-03-08 21:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210308_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spieler',
            name='code',
            field=models.UUIDField(default=uuid.UUID('0516f607-9b84-484a-a232-b1fd0a9dd28f'), unique=True),
        ),
    ]
