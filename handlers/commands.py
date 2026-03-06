import telebot
from openai import OpenAI


def register_handlers(bot: telebot.TeleBot, client: OpenAI, config):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Hi! \n"
                              "I'm your artificial assistant. What do you want to know today? \n"
                              "To ask a question, follow the instructions: /tell <question>")

    @bot.message_handler(commands=['tell'])
    def tell(message):
        question = message.text.split(' ', 1)[1]
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": config.API_KEY_OF_CLIENT.get_secret_value(),
                "X-Title": "Tg_Bot",
            },
            extra_body={},
            model=config.API_OF_MODEL.get_secret_value(),
            messages=[
              {
                "role": "user",
                "content": f"{question}"
              }
            ]
        )
        bot.reply_to(message, completion.choices[0].message.content)