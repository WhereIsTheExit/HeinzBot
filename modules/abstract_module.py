import json
from abc import ABC

from telegram import Update


class AbstractModule(ABC):
    mutedAccounts = []
    _commandList = ""
    keyFileName = "api-keys.json"

    def get_chat_id(self, update: Update):
        return update.message.chat_id

    def add_help_text(self, text):
        AbstractModule._commandList += text

    def get_api_key(self, key_name):
        f = open(self.keyFileName, "r")
        key_data = json.load(f)
        try:
            data = key_data[key_name]
            return data
        except:
            print(key_name + " not found")
            return ""

    def get_command_parameter(self, command: str, update) -> str:
        text = update.message.text
        b = update.message.bot.name
        if text.startswith(command + " "):
            return text[len(command) + 1:]
        if text.startswith(command + b + " "):
            return text[len(command + b) + 1:]

    def percent_encoding(self, text: str) -> str:
        """
        Encode the text into an url-transferable format.
        :param text: The text to encode
        :return: the encoded text
        """
        result = ''
        accepted = [c for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~'.encode('utf-8')]
        for char in text.encode('utf-8'):
            result += chr(char) if char in accepted else '%{}'.format(hex(char)[2:]).upper()
        return result
