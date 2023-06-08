import requests
import pathlib
import argparse


def fetch_spacex_last_launch(images_folder='./images',
                             launch_id='61eefaa89eb1064137a1bd73'):
    pathlib.Path(images_folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}/")
    launch_images = response.json()['links']['flickr']['original']

    for image_number, image_url in enumerate(launch_images):
        image_name = f'spacex_{image_number}{launch_id}.jpeg'
        response = requests.get(image_url)
        with open(f'{images_folder}/{image_name}', 'wb') as file:
            file.write(response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--identifier", required=False)
    args = parser.parse_args()
    if args.identifier:
        fetch_spacex_last_launch(launch_id=args.identifier)
    else:
        fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
