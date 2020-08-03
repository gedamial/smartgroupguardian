from telegram.ext import Filters,CommandHandler

import strings


def ping(update,context):
    update.effective_message.reply_text(strings.get(strings.ping_success,update.effective_chat))


handlers=[
    CommandHandler('ping',ping,Filters.private)
]
