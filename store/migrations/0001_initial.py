# Generated by Django 4.2.5 on 2023-09-19 09:07

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("phonenumber", models.CharField(max_length=10)),
                ("discount", models.FloatField()),
                ("creditlimit", models.DecimalField(decimal_places=1, max_digits=5)),
                ("tinnumber", models.BigIntegerField()),
                ("vrnnumber", models.BigIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "sku",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("purchase_order", models.CharField(max_length=100)),
                ("purchase_date", models.DateField(auto_now_add=True)),
                ("supplier", models.CharField(max_length=255)),
                ("quantity", models.BigIntegerField()),
                ("unit_price", models.DecimalField(decimal_places=1, max_digits=8)),
                (
                    "discount",
                    models.DecimalField(decimal_places=1, default=0.0, max_digits=8),
                ),
                ("total", models.DecimalField(decimal_places=1, max_digits=8)),
                ("expire_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=100)),
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("mail", models.CharField(max_length=255)),
                (
                    "recoveryToken",
                    models.CharField(
                        default=store.models.generate_unique_token,
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "user_role",
                    models.CharField(
                        choices=[("1", "Admin"), ("2", "Worker")],
                        default="2",
                        max_length=255,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "sale_order",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("sale_date", models.DateField(auto_now_add=True)),
                ("quantity", models.BigIntegerField()),
                ("discount", models.FloatField()),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "sku",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="store.purchase"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reserved",
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
                ("quantity", models.BigIntegerField()),
                (
                    "sku",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.purchase"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("item_name", models.CharField(max_length=255)),
                ("item_description", models.CharField(max_length=255)),
                ("slug", models.SlugField(default="-")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("food", "Food"),
                            ("beverage", "Beverage"),
                            ("household", "Household"),
                            ("other", "Other"),
                        ],
                        default="food",
                        max_length=255,
                    ),
                ),
                (
                    "uom",
                    models.CharField(
                        choices=[
                            ("pcs", "Pieces"),
                            ("kg", "Kilograms"),
                            ("m", "Meters"),
                            ("L", "Liters"),
                            ("lbs", "Pounds"),
                            ("gal", "Gallons"),
                        ],
                        default="kg",
                        max_length=255,
                    ),
                ),
                ("reorder_point", models.BigIntegerField()),
                (
                    "total_purchases",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "total_sales",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                ("stock_available_main", models.BigIntegerField(default=0)),
                ("stock_available_for_sale", models.BigIntegerField(default=0)),
                (
                    "stock_available_value",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                ("best_selling_product", models.BooleanField(default=False)),
                (
                    "sku",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.purchase"
                    ),
                ),
            ],
        ),
    ]
