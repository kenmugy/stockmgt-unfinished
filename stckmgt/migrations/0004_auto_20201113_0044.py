# Generated by Django 3.1.2 on 2020-11-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stckmgt', '0003_remove_stock_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='issued_to',
            field=models.CharField(max_length=50, verbose_name='Issued to'),
        ),
    ]
