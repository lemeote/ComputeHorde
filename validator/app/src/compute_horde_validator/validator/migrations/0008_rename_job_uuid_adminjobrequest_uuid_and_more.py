# Generated by Django 4.2.11 on 2024-05-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("validator", "0007_adminjobrequest"),
    ]

    operations = [
        migrations.RenameField(
            model_name="adminjobrequest",
            old_name="job_uuid",
            new_name="uuid",
        ),
        migrations.AlterField(
            model_name="adminjobrequest",
            name="timeout",
            field=models.PositiveIntegerField(default=300, help_text="timeout in seconds"),
        ),
    ]
