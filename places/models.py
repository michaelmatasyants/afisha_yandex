from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    description_short = models.CharField(verbose_name='Короткое описание',
                                         max_length=250)
    description_long = models.TextField(verbose_name='Длинное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
