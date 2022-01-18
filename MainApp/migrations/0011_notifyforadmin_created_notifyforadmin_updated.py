# Generated by Django 4.0.1 on 2022-01-18 00:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_alter_notifyforadmin_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifyforadmin',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifyforadmin',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last edit'),
        ),
    ]