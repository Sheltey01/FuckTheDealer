# Generated by Django 3.1.5 on 2021-03-08 21:22

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210308_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spieler',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]
