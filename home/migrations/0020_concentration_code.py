# Generated by Django 2.0.4 on 2018-04-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_concentration_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='concentration',
            name='code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]