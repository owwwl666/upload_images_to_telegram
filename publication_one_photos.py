import os
import random
import pathlib
import environs
import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    directory = env('PATH_TO_PHOTOS_DIRECTORY')
    photos = os.listdir(pathlib.Path.cwd().joinpath('images'))

    try:
        bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(env('PATH_TO_PHOTO'), 'rb'))
    except environs.EnvError:
        bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(f'{directory}{random.choice(photos)}', 'rb'))


if __name__ == '__main__':
    main()
