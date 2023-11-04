from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    '''Places'''
    title = models.CharField(verbose_name='Название',
                             max_length=250,
                             unique=True)
    short_description = models.TextField(verbose_name='Короткое описание',
                                         blank=True)
    long_description = HTMLField(verbose_name='Длинное описание',
                                 blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self) -> str:
        return f'{self.title}'


class Image(models.Model):
    '''Place images'''
    place = models.ForeignKey(Place,
                              verbose_name='Место',
                              on_delete=models.CASCADE,
                              related_name='images')
    file = models.ImageField(verbose_name='Картинка',
                             upload_to='',
                             unique=True)
    file_position = models.IntegerField(verbose_name='Позиция',
                                        default=0,
                                        db_index=True,
                                        blank=True)

    class Meta:
        ordering = ['file_position']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        unique_together = ('file', 'place')
