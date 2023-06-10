import os
import time
import random
import telegram
import pathlib
from environs import Env
from opening_and_reading_file import reads_file


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    directory = pathlib.Path.cwd().joinpath(env('PATH_TO_PHOTOS_DIRECTORY'))
    photos = os.listdir(pathlib.Path.cwd().joinpath(env('PATH_TO_PHOTOS_DIRECTORY')))
    default_sleep = 4 * 3600

    while True:
        try:
            random.shuffle(photos)
            for photo in photos:
                bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int),
                               photo=reads_file(pathlib.Path(directory).joinpath(photo)))
                time.sleep(default_sleep)
        except telegram.error.NetworkError:
            time.sleep(30)
            continue


if __name__ == '__main__':
    main()
