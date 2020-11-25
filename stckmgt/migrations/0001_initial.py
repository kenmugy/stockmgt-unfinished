# Generated by Django 3.1.2 on 2020-11-12 21:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(choices=[('', ''), ('V160YK', 'V160YK'), ('V001YK', 'V001YK'), ('V109YK', 'V109YK'), ('V121YK', 'V121YK'), ('V131YK', 'V131YK'), ('V133YK', 'V133YK'), ('V196YK', 'V196YK')], max_length=50, null=True)),
                ('color', models.CharField(max_length=55, null=True)),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity MTS')),
                ('opening_stck', models.IntegerField(default=0)),
                ('closing_stck', models.IntegerField(default=0)),
                ('issued_to', models.CharField(blank=True, max_length=50, verbose_name='Issued to')),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stckmgt.category')),
                ('issued_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
