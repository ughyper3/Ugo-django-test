# Generated by Django 3.2.5 on 2022-07-21 09:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleet', '0002_auto_20211109_1456'),
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('deleted', models.BooleanField(default=False)),
                ('departure_time', models.DateTimeField(default=None, null=True)),
                ('arrival_time', models.DateTimeField(default=None, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.bus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('deleted', models.BooleanField(default=False)),
                ('stop_location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geography.place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusSubRoute',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('deleted', models.BooleanField(default=False)),
                ('passage_datetime', models.DateTimeField()),
                ('bus_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.busshift')),
                ('bus_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.busstop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='busshift',
            name='bus_stops',
            field=models.ManyToManyField(through='ride.BusSubRoute', to='ride.BusStop'),
        ),
        migrations.AddField(
            model_name='busshift',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.driver'),
        ),
    ]
