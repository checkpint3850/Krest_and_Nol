# Generated by Django 5.0.6 on 2024-08-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', through='news.PostCategory', to='news.category'),
        ),
    ]
