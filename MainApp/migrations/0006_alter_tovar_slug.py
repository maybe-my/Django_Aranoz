# Generated by Django 4.0.1 on 2022-01-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_alter_tovar_kod_alter_tovar_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
    ]
