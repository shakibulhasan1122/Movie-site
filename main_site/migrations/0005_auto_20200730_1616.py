# Generated by Django 3.0.6 on 2020-07-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_auto_20200730_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieslink',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
