# Generated by Django 3.1.7 on 2021-02-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addevent', '0004_auto_20210228_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_event',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]