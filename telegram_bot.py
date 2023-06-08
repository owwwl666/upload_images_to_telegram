import telegram
from environs import Env

env = Env()
env.read_env()

bot = telegram.Bot(token=env('TELEGRAM_BOT_TOKEN'))
updates = bot.get_updates()

bot.send_message(text='Hello', chat_id=env('TELEGRAM_CHAT_ID', int))
