# Generated by Django 2.2.13 on 2020-12-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('type', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('available', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'roomtype',
                'managed': True,
            },
        ),
    ]