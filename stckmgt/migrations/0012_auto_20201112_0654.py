# Generated by Django 3.1.2 on 2020-11-12 03:54

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stckmgt', '0011_auto_20201112_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issued_by',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]