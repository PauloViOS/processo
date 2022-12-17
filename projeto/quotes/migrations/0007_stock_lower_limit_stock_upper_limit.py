# Generated by Django 4.1.4 on 2022-12-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_alter_historicalprice_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='lower_limit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='upper_limit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]