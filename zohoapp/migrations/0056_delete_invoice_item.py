# Generated by Django 4.1.7 on 2023-10-21 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0055_retainer_payment_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='invoice_item',
        ),
    ]
