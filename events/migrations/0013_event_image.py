# Generated by Django 4.2.7 on 2023-11-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
