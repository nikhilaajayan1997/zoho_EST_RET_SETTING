# Generated by Django 4.1.7 on 2023-10-12 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0036_invoice_invoice_item_invoice_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='invoice_item',
        ),
    ]