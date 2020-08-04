from telegram.ext import MessageHandler,Filters
from data_base import get_welcome_message


def welcome(update,context):
    # test to check if it's better to send one message per each user in message.new_chat_members or
    # one single message per update, since update.message.new_chat_members could contain many members
    welcome_message=get_welcome_message(update.effective_chat.id)
    if welcome_message:
        update.message.reply_text(welcome_message)


handlers=[
    MessageHandler(Filters.status_update.new_chat_members,welcome)
]
