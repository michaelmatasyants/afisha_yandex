from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ['place', 'file_position']
