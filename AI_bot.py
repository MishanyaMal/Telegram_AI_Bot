from openai import OpenAI
import telebot

from config_reader import config
from handlers import commands


bot = telebot.TeleBot(
    token=config.BOT_TOKEN.get_secret_value()
)

client = OpenAI(
    base_url=config.BASE_URL_FROM_OPENROUTER.get_secret_value(),
    api_key=config.API_KEY_OF_CLIENT.get_secret_value(),
)

def main():

    commands.register_handlers(bot, client, config)

    return bot.polling(none_stop=True)

if __name__ == '__main__':
    main()