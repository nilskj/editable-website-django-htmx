# Generated by Django 4.2.4 on 2023-08-06 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("editor", "0003_page_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="page",
            name="data",
        ),
    ]
