# Generated by Django 4.0.3 on 2022-03-23 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_note_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='date_time',
        ),
    ]
