# Generated by Django 3.1.5 on 2021-03-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210308_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='spieler',
            name='host',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='spieler',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='spieler',
            name='type',
            field=models.SmallIntegerField(null=True),
        ),
    ]
