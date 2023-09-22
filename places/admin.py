from django.contrib import admin
from places.models import Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ["title", "lng", "lat"]
