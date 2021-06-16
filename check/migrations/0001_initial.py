# Generated by Django 3.1.2 on 2021-06-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('standard', models.IntegerField()),
                ('percentage', models.TextField(max_length=4)),
                ('email', models.CharField(max_length=20)),
                ('password', models.TextField(verbose_name=10)),
            ],
        ),
    ]