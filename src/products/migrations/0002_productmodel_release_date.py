# Generated by Django 5.0.2 on 2024-02-16 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='release_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]