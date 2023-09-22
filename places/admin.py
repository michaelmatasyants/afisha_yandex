from django.contrib import admin
from places.models import Place, Image


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ['place']
