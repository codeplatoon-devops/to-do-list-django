# Generated by Django 4.2.1 on 2023-05-05 13:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('to_do_list_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='To_do',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.TimeField(default=datetime.time(13, 31, 20, 496311))),
                ('completed_at', models.TimeField()),
                ('to_do_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='to_do_list_app.to_do_list')),
            ],
        ),
    ]
