# Generated by Django 5.1.5 on 2025-07-21 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='car.carcondition'),
        ),
    ]
