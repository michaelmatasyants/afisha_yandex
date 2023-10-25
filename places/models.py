from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    '''Places'''
    place_id = models.CharField(max_length=250, unique=True)
    title = models.CharField(verbose_name='Название',
                             max_length=250)
    point_title = models.CharField(verbose_name='Назваение точки на карте',
                                   max_length=250,
                                   blank=True)
    description_short = models.TextField(verbose_name='Короткое описание',
                                         blank=True)
    description_long = HTMLField(verbose_name='Длинное описание',
                                 blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    '''Place images'''
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images')
    file = models.ImageField(verbose_name='Картинка',
                             upload_to='')
    file_position = models.IntegerField(verbose_name='Позиция',
                                        null=False,
                                        blank=False,
                                        default=0)

    class Meta:
        ordering = ['file_position']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
