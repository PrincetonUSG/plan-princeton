# Generated by Django 2.0.4 on 2018-05-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180509_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='concentration',
            name='sample_plans',
            field=models.ManyToManyField(to='home.Plan'),
        ),
    ]
