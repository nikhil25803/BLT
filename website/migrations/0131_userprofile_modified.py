# Generated by Django 5.0.7 on 2024-08-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0130_userprofile_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
