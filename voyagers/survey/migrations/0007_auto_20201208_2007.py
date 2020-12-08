# Generated by Django 3.0.5 on 2020-12-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20201207_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='survey',
            name='country',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='survey',
            name='departure',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='survey',
            name='futureCompanionDescription',
            field=models.TextField(blank=True, default='Outgoing, passionate about food'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='survey',
            name='tour',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]