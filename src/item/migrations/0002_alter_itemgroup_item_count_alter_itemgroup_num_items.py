# Generated by Django 4.0.6 on 2023-07-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemgroup',
            name='item_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemgroup',
            name='num_items',
            field=models.IntegerField(default=0),
        ),
    ]
