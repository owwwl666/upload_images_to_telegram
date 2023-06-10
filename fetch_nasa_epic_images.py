import requests
import pathlib
import argparse
from datetime import datetime
from download_file import downloads_file
from environs import Env


def downloads_images_from_nasa_epic(images_folder,
                                    api_key='DEMO_KEY', photos_quantity=3):
    pathlib.Path(images_folder).mkdir(parents=True, exist_ok=True)
    earth_photos_url = requests.get(url='https://api.nasa.gov/EPIC/api/natural',
                                    params={'api_key': api_key})
    earth_photos_url.raise_for_status()
    earth_photos = earth_photos_url.json()[:photos_quantity]

    for image in earth_photos:
        image_date = datetime.fromisoformat(image['date']) \
            .strftime('%Y/%m/%d')
        image_name = image['image']
        image_id = image['identifier']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                         f'{image_date}/png/{image_name}.png'
        photo_name = f'epic_{image_id}.png'
        downloads_file(epic_image_url, images_folder, photo_name, api_key=api_key)


def main():
    env = Env()
    env.read_env()
    images_folder = pathlib.Path.cwd().joinpath(env('PATH_TO_PHOTOS_DIRECTORY'))

    parser = argparse.ArgumentParser()
    parser.add_argument("-key", "--api_key", required=False, default='DEMO_KEY')
    parser.add_argument("-qp", "--photos_quantity", required=False, default=3, type=int)
    args = parser.parse_args()
    downloads_images_from_nasa_epic(images_folder, api_key=args.api_key, photos_quantity=args.photos_quantity)


if __name__ == '__main__':
    main()
