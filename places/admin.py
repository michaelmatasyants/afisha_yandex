from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from places.models import Place, Image


class ImageInline(SortableStackedInline):
    '''Inline for images to show in Place model'''
    model = Image
    readonly_fields = ['preview']

    def preview(self, image_obj):
        '''display preview of image'''
        return format_html('<img src="{}" width="200" height="200" />',
                           image_obj.file.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    '''Admin panel for Place model'''
    list_display = ['title', 'lng', 'lat']
    search_fields = ['title']
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    '''Admin panel for Image model'''
    list_display = ['place', 'file_position', ]
    autocomplete_fields = ['place', ]
