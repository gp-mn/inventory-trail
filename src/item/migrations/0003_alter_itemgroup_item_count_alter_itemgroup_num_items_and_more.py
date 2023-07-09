# Generated by Django 4.0.6 on 2023-07-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_itemgroup_item_count_alter_itemgroup_num_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemgroup',
            name='item_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='itemgroup',
            name='num_items',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='itemgroup',
            name='status',
            field=models.TextField(choices=[('AVAIL', 'available'), ('UNAVAIL', 'unavailable')], default='AVAIL'),
        ),
    ]
