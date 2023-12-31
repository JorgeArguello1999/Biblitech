# Generated by Django 4.2.4 on 2023-09-08 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Counts",
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
                ("grade", models.CharField(max_length=100)),
                ("teacher", models.CharField(max_length=100)),
                ("mount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payed", models.BooleanField(default=False)),
                ("date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
