# Generated by Django 4.2.1 on 2023-05-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_water_consumed', models.IntegerField()),
                ('total_cost', models.IntegerField()),
            ],
        ),
    ]
