import requests
import pathlib
import argparse
from datetime import datetime


def downloads_images_from_nasa_epic(images_folder='./images', api_key='DEMO_KEY'):
    pathlib.Path(images_folder).mkdir(parents=True, exist_ok=True)
    epic_url = requests.get(url='https://api.nasa.gov/EPIC/api/natural',
                            params={'api_key': api_key}).json()[:3]
    for image in epic_url:
        image_date = datetime.fromisoformat(image.get('date')) \
            .strftime('%Y/%m/%d')
        image_name = image.get('image')
        image_id = image.get('identifier')
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                         f'{image_date}/png/{image_name}.png'
        response = requests.get(epic_image_url, params={'api_key': api_key})
        with open(f'{images_folder}/epic_{image_id}.png', 'wb') as file:
            file.write(response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", required=False)
    args = parser.parse_args()
    if args.api_key:
        downloads_images_from_nasa_epic(api_key=args.api_key)
    else:
        downloads_images_from_nasa_epic()


if __name__ == '__main__':
    main()
