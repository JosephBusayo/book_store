# Generated by Django 2.2 on 2020-12-05 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='co_author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='release',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
