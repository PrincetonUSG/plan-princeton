# Generated by Django 2.0.4 on 2018-04-20 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180420_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concentration',
            name='code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Department'),
        ),
    ]