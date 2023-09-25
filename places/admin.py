from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['show_image']

    def show_image(self, obj):
        return format_html(
                f'<img src="{obj.file.url}" width="200" height="200" />')



@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ['place', 'file_position']
