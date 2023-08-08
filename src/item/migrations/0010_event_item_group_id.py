# Generated by Django 4.0.6 on 2023-08-08 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='item_group_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='item.itemgroup'),
            preserve_default=False,
        ),
    ]