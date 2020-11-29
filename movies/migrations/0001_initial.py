# Generated by Django 3.1.3 on 2020-11-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=200)),
                ('other_titles', models.CharField(blank=True, max_length=200)),
                ('production_year', models.CharField(blank=True, max_length=9)),
                ('production_country', models.CharField(blank=True, default='', max_length=3)),
                ('genre', models.CharField(blank=True, choices=[('horror', 'horror'), ('sci-fi', 'sci-fi'), ('thriller', 'thriller'), ('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama')], max_length=200)),
                ('medium', models.CharField(blank=True, choices=[('dvd', 'dvd'), ('dvd-r', 'dvd-r'), ('cd', 'cd'), ('cd-r', 'cd-r'), ('vcd', 'vcd'), ('vhs', 'vhs')], max_length=200)),
                ('rating', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('comments', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('main_title',),
            },
        ),
    ]
