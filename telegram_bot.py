import telegram
from environs import Env

env = Env()
env.read_env()

bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
updates = bot.get_updates()

bot.send_photo(chat_id=env('TELEGRAM_CHAT_ID', int), photo=open(env('PATH_TO_PHOTO', str), 'rb'))
