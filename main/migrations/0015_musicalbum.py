# Generated by Django 3.1.7 on 2021-05-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_picturetag'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=True)),
                ('cover', models.ImageField(blank=True, upload_to='music/covers')),
            ],
        ),
    ]