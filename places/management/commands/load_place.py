import logging
#import os
from urllib.parse import urlparse
from django.core.management.base import BaseCommand, CommandParser
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile

import requests

from places.models import Place, Image


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class Command(BaseCommand):
    help='Helps to add new places from json files'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_places', nargs='*')

    def handle(self, *args, **options):
        places = options['json_places']
        for place in places:
            place_response = requests.get(url=place, timeout=60)
            place_response.raise_for_status()
            new_place = place_response.json()

            defaults = dict(
                title=new_place['title'],
                short_description=new_place['description_short'],
                long_description=new_place['description_long'],
                lng=new_place['coordinates']['lng'],
                lat=new_place['coordinates']['lat']
            )
            added_place, place_created = Place.objects.update_or_create(
                title=new_place['title'],
                defaults=defaults
            )

            images = new_place['imgs']
            for image_url in images:
                image_response = requests.get(url=image_url, timeout=120)
                image_response.raise_for_status()
                image_name = urlparse(image_url).path.split('/')[-1]

                image, _ = Image.objects.update_or_create(place=added_place,
                                                          file=image_name)
                image.file.save(image_name,
                                ContentFile(image_response.content),
                                save=True)
            if not place_created:
                logging.info(
                    msg=f'Place "{added_place}" was already added earlier')
                continue
            logging.info(msg=f'New place "{added_place}" added')
