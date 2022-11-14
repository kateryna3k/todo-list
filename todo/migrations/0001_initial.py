# Generated by Django 4.1.3 on 2022-11-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField()),
                ("is_done", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(related_name="tasks", to="todo.tag")),
            ],
        ),
    ]
