# Generated by Django 2.0.4 on 2018-04-20 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_concentration_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concentration',
            name='code',
        ),
    ]