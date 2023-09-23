from django.db import models


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
    description_long = models.TextField(verbose_name='Длинное описание',
                                        blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self) -> str:
        return f'{self.title}'


class Image(models.Model):
    '''Place images'''
    place = models.ForeignKey(Place,
                              null=True,
                              on_delete=models.CASCADE)
    file = models.ImageField(verbose_name='Картинка',
                             upload_to='')
