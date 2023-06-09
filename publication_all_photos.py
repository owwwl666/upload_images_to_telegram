import os
import time
import random
import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    directory = env('PATH_TO_PHOTOS_DIRECTORY')
    photos = os.listdir('./images')
    default_sleep = 4*3600

    while True:
        try:
            random.shuffle(photos)
            for photo in photos:
                bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(f'{directory}/{photo}', 'rb'))
                time.sleep(default_sleep)
        except telegram.error.NetworkError:
            time.sleep(30)
            continue



if __name__ == '__main__':
    main()
