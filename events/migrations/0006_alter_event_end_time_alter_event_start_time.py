# Generated by Django 4.2.7 on 2023-11-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_date_event_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
