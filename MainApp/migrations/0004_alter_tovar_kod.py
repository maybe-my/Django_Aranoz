# Generated by Django 4.0.1 on 2022-01-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_tovar_image_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='kod',
            field=models.FloatField(blank=True, db_index=True, default='', max_length=6, verbose_name='KOD tovar*'),
        ),
    ]