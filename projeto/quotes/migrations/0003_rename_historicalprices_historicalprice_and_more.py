# Generated by Django 4.1.4 on 2022-12-17 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_remove_stock_id_alter_stock_ticker_historicalprices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalPrices',
            new_name='HistoricalPrice',
        ),
        migrations.AddField(
            model_name='stock',
            name='company_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
