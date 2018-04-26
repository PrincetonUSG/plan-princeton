# Generated by Django 2.0.4 on 2018-04-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_concentration_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='req_list',
            name='course_list',
            field=models.ManyToManyField(blank=True, to='home.Course'),
        ),
        migrations.AlterField(
            model_name='req_list',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='req_list',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]