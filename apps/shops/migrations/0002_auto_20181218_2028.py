# Generated by Django 2.1.3 on 2018-12-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='image',
            field=models.ImageField(max_length=50, upload_to='shops/%Y/%m', verbose_name='logo'),
        ),
    ]
