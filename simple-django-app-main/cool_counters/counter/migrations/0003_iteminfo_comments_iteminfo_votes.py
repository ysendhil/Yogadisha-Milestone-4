# Generated by Django 4.2.7 on 2023-11-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_iteminfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminfo',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
