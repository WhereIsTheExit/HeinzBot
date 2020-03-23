from modules.abstract_module import AbstractModule
from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from utils.decorators import register_command, register_module, send_action


@register_module()
class CatBot(AbstractModule):
    @register_command(command="cat", short_desc="Sends a personalized cat. 😺",
                      long_desc="Depending on the given text, a personalized "
                                "cat gif is sent with the entered text on it.",
                      usage=["/cat $text", "/cat I am a cool cat!"])
    @send_action(action=ChatAction.UPLOAD_VIDEO)
    def cat_command(self, update: Update, context: CallbackContext):
        query = self.get_command_parameter("/cat", update)
        chat_id = update.message.chat_id
        if not query:
            img = 'https://cataas.com/c/gif'
        else:
            query = self.percent_encoding(query)
            img = 'https://cataas.com/c/gif/s/' + query
        context.bot.send_animation(chat_id=chat_id, animation=img)