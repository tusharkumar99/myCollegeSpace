# Generated by Django 3.1.6 on 2021-05-17 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('post', models.CharField(max_length=5000)),
                ('dated', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
