from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from places.models import Place


def show_main_page(request):
    '''Main_page view'''
    places = Place.objects.all()
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.point_title,
                "placeId": place.place_id,
                "detailsUrl": reverse(show_place_json, args=[place.id])
            }
        } for place in places]
    print('print output', reverse(show_place_json, args=[places[1].id]))
    context = {
        'places_geojson': {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'index.html', context=context)


def show_place_json(request, place_id):
    '''Place json view'''
    place = get_object_or_404(Place, pk=place_id)
    response = {
        "title": place.title,
        "imgs": [photo.file.url for photo in place.images.order_by('file_position')],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }
    return JsonResponse(response,
                        json_dumps_params={'ensure_ascii': False, 'indent': 4})
