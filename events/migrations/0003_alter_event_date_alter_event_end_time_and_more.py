# Generated by Django 4.2.7 on 2023-11-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_time_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='repeats',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
