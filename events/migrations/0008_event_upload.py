# Generated by Django 4.2.7 on 2023-11-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='upload',
            field=models.ImageField(default='', upload_to='static'),
            preserve_default=False,
        ),
    ]