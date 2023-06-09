import requests
import pathlib
import argparse
from download_file import downloads_file


def fetch_spacex_last_launch(images_folder='./images',
                             launch_id='6243adcaaf52800c6e919254'):
    pathlib.Path(images_folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    launch_images = response.json()['links']['flickr']['original']

    for image_number, image_url in enumerate(launch_images):
        image_name = f'spacex_{image_number}{launch_id}.jpeg'
        downloads_file(image_url, images_folder, image_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--identifier", required=False,default='6243adcaaf52800c6e919254')
    args = parser.parse_args()
    fetch_spacex_last_launch(launch_id=args.identifier)
    # if args.identifier:
    #     fetch_spacex_last_launch(launch_id=args.identifier)
    # else:
    #     fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
