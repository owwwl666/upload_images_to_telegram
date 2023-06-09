import os
import random
import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    directory = env('PATH_TO_PHOTOS_DIRECTORY')
    photos = os.listdir('./images')

    try:
        bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(env('PATH_TO_PHOTOS'), 'rb'))
    except:
        bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(f'{directory}{random.choice(photos)}', 'rb'))


if __name__ == '__main__':
    main()
