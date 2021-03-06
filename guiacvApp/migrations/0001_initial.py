# Generated by Django 3.1.7 on 2021-04-21 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Telephone1', models.CharField(max_length=200)),
                ('Telephone2', models.CharField(max_length=200)),
                ('Celular', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Website', models.TextField()),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=200)),
                ('Island', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Sub_Category', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Photo1', models.ImageField(upload_to='uploads/Photo1/')),
                ('Photo2', models.ImageField(blank=True, default='', null=True, upload_to='uploads/Photo2/')),
                ('Photo3', models.ImageField(blank=True, default='', null=True, upload_to='uploads/Photo3/')),
                ('Photo4', models.ImageField(blank=True, default='', null=True, upload_to='uploads/Photo4/')),
                ('time', models.DateField(blank=True, default=datetime.datetime(2021, 4, 21, 16, 1, 24, 97598))),
            ],
            options={
                'verbose_name_plural': 'form register',
            },
        ),
    ]
