# Generated by Django 3.1.3 on 2020-12-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]
