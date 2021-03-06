# Generated by Django 3.0.2 on 2020-02-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoQuakesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuakePredictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Magnitude', models.FloatField()),
                ('Depth', models.FloatField()),
                ('Score', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Quake_Predictions',
            },
        ),
    ]
