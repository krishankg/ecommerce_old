# Generated by Django 3.0 on 2020-01-03 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='price',
        ),
    ]
