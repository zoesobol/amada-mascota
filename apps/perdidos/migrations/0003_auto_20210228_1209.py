# Generated by Django 3.1.6 on 2021-02-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perdidos', '0002_auto_20210227_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotos',
            field=models.ImageField(upload_to='perdido'),
        ),
    ]