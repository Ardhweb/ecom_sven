# Generated by Django 4.2.7 on 2024-01-08 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='subcategory',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_no',
            field=models.CharField(default='fad6669e', editable=False, max_length=255),
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]