# Generated by Django 3.1.5 on 2021-03-08 21:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210308_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spieler',
            name='code',
            field=models.UUIDField(default=uuid.UUID('77f0a39d-d1f6-4de1-8219-79e74d5fb8e1'), unique=True),
        ),
    ]
