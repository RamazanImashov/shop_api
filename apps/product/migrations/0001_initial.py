# Generated by Django 4.2.5 on 2023-09-05 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "title",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Название категории"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=30, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "title",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Naming"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=30, primary_key=True, serialize=False
                    ),
                ),
                ("image", models.ImageField(upload_to="images/", verbose_name="Image")),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                ("in_stock", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="product.category",
                        verbose_name="Category",
                    ),
                ),
            ],
        ),
    ]
