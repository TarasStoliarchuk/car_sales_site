# Generated by Django 3.2.4 on 2021-06-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='slug',
            field=models.SlugField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]