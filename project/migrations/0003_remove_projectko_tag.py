# Generated by Django 2.1 on 2018-08-16 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180816_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectko',
            name='tag',
        ),
    ]