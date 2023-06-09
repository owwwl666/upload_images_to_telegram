import os
import random
import pathlib
import environs
import telegram
from environs import Env
from reading_file import reads_file


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    directory = pathlib.Path.cwd().joinpath(env('PATH_TO_PHOTOS_DIRECTORY'))
    photos = os.listdir(pathlib.Path.cwd().joinpath('images'))

    try:
        bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=reads_file(env('PATH_TO_PHOTO')))
    except environs.EnvError:
        bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int),
                       photo=reads_file(pathlib.Path(directory).joinpath(random.choice(photos))))


if __name__ == '__main__':
    main()
