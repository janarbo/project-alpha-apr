# Generated by Django 4.1.5 on 2023-01-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
