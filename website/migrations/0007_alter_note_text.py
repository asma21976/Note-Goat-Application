# Generated by Django 4.0.3 on 2022-03-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_note_content_alter_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]