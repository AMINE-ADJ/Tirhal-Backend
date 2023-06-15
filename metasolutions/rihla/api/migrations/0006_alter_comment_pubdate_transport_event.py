# Generated by Django 4.1.4 on 2023-06-15 12:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_comment_rating_alter_comment_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 12, 10, 55, 324155, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('placefrom', models.CharField(max_length=255)),
                ('placeto', models.CharField(max_length=255)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datefrom', models.DateTimeField()),
                ('dateto', models.DateTimeField()),
                ('place', models.CharField(max_length=255)),
                ('idRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.region')),
            ],
        ),
    ]
