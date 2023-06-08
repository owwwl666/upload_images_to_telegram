import os
import random
import telegram
from environs import Env

env = Env()
env.read_env()

bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))

photos = os.listdir('./images')

try:
    bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(env('PATH_TO_PHOTOS'), 'rb'))
except:
    random.shuffle(photos)
    photo = photos[0]
    bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(f'./images/{photo}', 'rb'))
