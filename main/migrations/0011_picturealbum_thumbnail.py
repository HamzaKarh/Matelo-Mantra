# Generated by Django 3.1.7 on 2021-05-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210505_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturealbum',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnail'),
        ),
    ]
