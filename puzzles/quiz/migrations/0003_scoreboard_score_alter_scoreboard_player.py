# Generated by Django 4.2.1 on 2024-04-27 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("quiz", "0002_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="scoreboard",
            name="score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="scoreboard",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
