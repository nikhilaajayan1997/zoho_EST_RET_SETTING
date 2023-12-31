# Generated by Django 4.1.7 on 2023-10-09 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0027_delete_setting_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='setting_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(blank=True, max_length=25, null=True)),
                ('pricelist', models.CharField(blank=True, max_length=25, null=True)),
                ('offline_banking', models.CharField(blank=True, max_length=25, null=True)),
                ('banking', models.CharField(blank=True, max_length=25, null=True)),
                ('customers', models.CharField(blank=True, max_length=25, null=True)),
                ('estimates', models.CharField(blank=True, max_length=25, null=True)),
                ('retainer_invoices', models.CharField(blank=True, max_length=25, null=True)),
                ('sales_orders', models.CharField(blank=True, max_length=25, null=True)),
                ('delivery_challans', models.CharField(blank=True, max_length=25, null=True)),
                ('invoices', models.CharField(blank=True, max_length=25, null=True)),
                ('credit_notes', models.CharField(blank=True, max_length=25, null=True)),
                ('recurring_invoices', models.CharField(blank=True, max_length=25, null=True)),
                ('vendors', models.CharField(blank=True, max_length=25, null=True)),
                ('vendor_credits', models.CharField(blank=True, max_length=25, null=True)),
                ('expenses', models.CharField(blank=True, max_length=25, null=True)),
                ('recurring_expenses', models.CharField(blank=True, max_length=25, null=True)),
                ('purchase_orders', models.CharField(blank=True, max_length=25, null=True)),
                ('payment_made', models.CharField(blank=True, max_length=25, null=True)),
                ('bills', models.CharField(blank=True, max_length=25, null=True)),
                ('recurring_bills', models.CharField(blank=True, max_length=25, null=True)),
                ('projects', models.CharField(blank=True, max_length=25, null=True)),
                ('chart_of_accounts', models.CharField(blank=True, max_length=25, null=True)),
                ('employees', models.CharField(blank=True, max_length=25, null=True)),
                ('employees_loan', models.CharField(blank=True, max_length=25, null=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
