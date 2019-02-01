# Generated by Django 2.1.3 on 2019-01-15 17:50

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190115_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='image/default.jpg', null=True, upload_to=users.models.get_image_name, verbose_name='头像'),
        ),
    ]