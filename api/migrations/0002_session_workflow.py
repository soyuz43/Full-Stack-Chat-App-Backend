# Generated by Django 4.2.16 on 2024-12-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='workflow',
            field=models.JSONField(default=dict),
        ),
    ]