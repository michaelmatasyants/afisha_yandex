# Generated by Django 4.2.5 on 2023-09-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_image_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file_position',
            field=models.IntegerField(null=True, verbose_name='Позиция'),
        ),
    ]