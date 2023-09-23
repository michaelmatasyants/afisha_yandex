from django.shortcuts import render
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
                "placeId": place.id,
                "detailsUrl": f"static/places/{place.id}.json"
                }
        } for place in places]

    context = {'places_geojson': {
                    "type": "FeatureCollection",
                    "features": features
                    }
    }
    return render(request, 'index.html', context=context)
