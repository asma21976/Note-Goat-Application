# Generated by Django 4.0.3 on 2022-03-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_note_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
