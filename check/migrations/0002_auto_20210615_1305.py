# Generated by Django 3.1.2 on 2021-06-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='password',
            field=models.TextField(max_length=10),
        ),
    ]