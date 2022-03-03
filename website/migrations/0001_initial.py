# Generated by Django 4.0.2 on 2022-03-02 17:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file_name', models.CharField(default='New Note', max_length=50)),
                ('text', models.TextField(blank=True)),
                ('public', models.BooleanField(default=False)),
            ],
        ),
    ]
