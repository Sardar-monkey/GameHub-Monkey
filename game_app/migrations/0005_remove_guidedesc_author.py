# Generated by Django 5.1.2 on 2024-10-30 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0004_guidedesc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidedesc',
            name='author',
        ),
    ]
