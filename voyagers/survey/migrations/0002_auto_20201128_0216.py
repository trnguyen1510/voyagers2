# Generated by Django 3.0.5 on 2020-11-28 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer_Count',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
