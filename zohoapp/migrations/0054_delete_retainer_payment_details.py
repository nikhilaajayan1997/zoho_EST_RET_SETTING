# Generated by Django 4.1.7 on 2023-10-17 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0053_retainerinvoice_retaineritems_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='retainer_payment_details',
        ),
    ]
