import telegram
from telegram.ext import CommandHandler
import json
import requests

import api_key_reader

from modules.default_module import DefaultModule
from utils.decorators import register_module


@register_module(active=False)
class SpoontacularBot(DefaultModule):
    url = "https://api.spoonacular.com/"

    def add_command(self, dp):
        instance = SpoontacularBot()
        dp.add_handler(CommandHandler('meals', instance.random_receipt))
        return dp

    def random_receipt(self, bot, update):
        chat_id = update.message.chat_id
        key = api_key_reader.read_key("spoon")
        extender = "{}recipes/random?apiKey={}&number=4".format(self.url, key)
        data = requests.get(extender)
        jsonData = json.loads(data.text)

        response = "Meals I found randomly \n"

        for recipe in jsonData['recipes']:
            response += "*" + recipe['title'] + "*" + "\n"
            response += recipe['sourceUrl'] + "\n"
            response += "\n"

        bot.send_message(chat_id=chat_id, text=response, parse_mode=telegram.ParseMode.MARKDOWN)
