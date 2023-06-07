import os
import requests
import pathlib
from urllib.parse import urlsplit


def get_file_permission(file_url: str):
    return os.path.splitext(urlsplit(file_url).path)[1]


def fetch_spacex_last_launch(images_folder: str, launch_id: str):
    pathlib.Path(images_folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}/")
    launch_images = response.json()['links']['flickr']['original']

    for image_number, image_url in enumerate(launch_images):
        image_name = f'spacex_{image_number}.jpeg'
        response = requests.get(image_url)
        with open(f'./images/{image_name}', 'wb') as file:
            file.write(response.content)


fetch_spacex_last_launch('./images', '5eb87ce4ffd86e000604b337')
