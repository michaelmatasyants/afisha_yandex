from urllib.parse import urlparse
from where_to_go.settings import MEDIA_ROOT

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "where_to_go.settings")

import django
django.setup()

import requests
from places.models import Place, Image
import logging


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    places = [
        'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json',
        'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%97%D0%B0%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BB%D0%B0%D0%B3%D0%B5%D1%80%D1%8C%20%C2%AB%D0%A1%D0%BA%D0%B0%D0%B7%D0%BA%D0%B0%C2%BB.json',
        'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9C%D0%B5%D1%81%D1%82%D0%B0%2C%20%D0%B3%D0%B4%D0%B5%20%D1%81%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%81%D1%8F%20%20%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%20%C2%AB%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%E2%80%9E%D0%AB%E2%80%9C%20%D0%B8%C2%A0%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%A8%D1%83%D1%80%D0%B8%D0%BA%D0%B0%C2%BB.json',
        '',
    ]
    for place in places:
        place_response = requests.get(url=place, timeout=60)
        place_response.raise_for_status()
        new_place = place_response.json()

        added_place, place_created = Place.objects.get_or_create(
            title=new_place['title'],
            description_short=new_place['description_short'],
            description_long=new_place['description_long'],
            lng=new_place['coordinates']['lng'],
            lat=new_place['coordinates']['lat']
        )

        images = new_place['imgs']
        for image_url in images:
            image_response = requests.get(url=image_url, timeout=120)
            image_response.raise_for_status()
            image_name = urlparse(image_url).path.split('/')[-1]
            with open(os.path.join(MEDIA_ROOT, image_name), 'wb') as img:
                img.write(image_response.content)
                added_place.images.save(image_name, content=img, save=True)
            #added_image, _ = Image.objects.get_or_create(
            #    place=added_place,
            #    file=image_name
            #)
        if not place_created:
            logging.info(msg=f'Place "{added_place}" was already added earlier')
            continue
        logging.info(msg=f'New place "{added_place}" added')

if __name__ == "__main__":
    main()
