# Generated by Django 2.0.7 on 2018-07-17 23:00

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketPlaceListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255, null=True)),
                ('rarity', models.IntegerField()),
                ('price_finney', models.IntegerField()),
                ('num_clones_allowed', models.IntegerField(blank=True, null=True)),
                ('num_clones_in_wild', models.IntegerField(blank=True, null=True)),
                ('owner_address', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255, null=True)),
                ('cloned_from_id', models.IntegerField()),
                ('sent_from_address', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
