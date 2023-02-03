# Generated by Django 4.1.6 on 2023-02-01 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("kana_workout_builder_app", "0002_rename_text_workout_title_exercise"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="date_added",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
