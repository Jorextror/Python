# Generated by Django 4.0.4 on 2022-05-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_valoration_valoration'),
    ]

    operations = [
        migrations.AddField(
            model_name='valoration',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
