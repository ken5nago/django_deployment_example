# Generated by Django 3.1.4 on 2020-12-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(),
        ),
    ]
