# Generated by Django 4.1.4 on 2022-12-19 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0011_stock_portfolio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stock",
            name="lower_limit",
        ),
        migrations.RemoveField(
            model_name="stock",
            name="upper_limit",
        ),
        migrations.CreateModel(
            name="TunnelLimits",
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
                (
                    "upper_limit",
                    models.DecimalField(decimal_places=2, default=None, max_digits=10),
                ),
                (
                    "lower_limit",
                    models.DecimalField(decimal_places=2, default=None, max_digits=10),
                ),
                (
                    "portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.portfolio",
                    ),
                ),
                (
                    "ticker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="quotes.stock"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="tunnellimits",
            constraint=models.UniqueConstraint(
                fields=("portfolio", "ticker", "upper_limit", "lower_limit"),
                name="tunnel",
            ),
        ),
    ]
