# Generated by Django 3.2.4 on 2022-01-19 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220119_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='text',
            field=models.TextField(blank=True, max_length=350),
        ),
    ]
