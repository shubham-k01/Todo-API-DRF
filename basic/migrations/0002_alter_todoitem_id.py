# Generated by Django 4.2.7 on 2023-11-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
