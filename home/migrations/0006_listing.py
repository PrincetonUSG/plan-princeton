# Generated by Django 2.0.4 on 2018-04-20 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180420_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department')),
                ('x', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Course')),
            ],
        ),
    ]