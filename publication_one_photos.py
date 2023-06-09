import os
import random
import pathlib
import environs
import telegram
from environs import Env
from opening_and_reading_file import reads_file


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
    chat_id = env('TELEGRAM_CHAT_ID')
    directory = pathlib.Path.cwd().joinpath(env('PATH_TO_PHOTOS_DIRECTORY', './images'))
    photos = os.listdir(directory)

    try:
        photo_path = env('PATH_TO_PHOTOS')
    except environs.EnvError:
        photo_path = pathlib.Path(directory).joinpath(random.choice(photos))
    bot.send_photo(chat_id=chat_id, photo=reads_file(photo_path))

    if __name__ == '__main__':
        main()
