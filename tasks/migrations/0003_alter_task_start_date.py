# Generated by Django 4.1.5 on 2023-01-24 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_task_due_date_task_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]