# Generated by Django 2.0.5 on 2018-05-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(default='professor'),
        ),
    ]
