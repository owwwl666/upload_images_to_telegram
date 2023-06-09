import os
import time
import random
import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    photos = os.listdir('./images')

    while True:
        try:
            random.shuffle(photos)
            for photo in photos:
                bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(f'./images/{photo}', 'rb'))
                time.sleep(int(env('PUBLICATION_FREQUENCY')) * 60)
        except telegram.error.NetworkError:
            time.sleep(30)
            continue



if __name__ == '__main__':
    main()
