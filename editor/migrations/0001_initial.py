# Generated by Django 4.2.4 on 2023-08-06 19:56

from django.db import migrations, models
import prose.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("title", models.CharField(max_length=200)),
                ("data", prose.fields.RichTextField()),
            ],
        ),
    ]
