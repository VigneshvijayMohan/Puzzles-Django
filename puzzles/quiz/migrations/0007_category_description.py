# Generated by Django 4.2.1 on 2024-05-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0006_scoreboard_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.CharField(default=0, max_length=200),
        ),
    ]
