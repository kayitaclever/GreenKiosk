# Generated by Django 4.2.3 on 2023-07-07 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('inventory', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor'),
        ),
    ]
