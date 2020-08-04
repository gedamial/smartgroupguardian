from telegram import ParseMode
from telegram.ext import Filters
import strings
from data_base import get_macro,get_rules
from utils import GroupMessageHandler,GroupCommandHandler,PrivateCommandHandler


def ping(update,context):
    update.effective_message.reply_text(strings.get(strings.ping_success,update.effective_chat))


def macro(update,context):
    content=get_macro(update.effective_chat.id,update.effective_message.text)
    if content:
        update.effective_message.reply_text(content)


def rules(update,context):
    rules=get_rules(update.effective_chat.id)
    if rules:
        update.effective_message.reply_text(rules)


def alert_admin(update,context):
    chat=update.effective_chat
    admins=context.bot.get_chat_administrators(chat.id)
    for admin in admins:
        try:
            context.bot.send_message(admin.user.id,strings.get(strings.user_needs_help,chat,
                                                               update.effective_user.first_name,
                                                               update.effective_message.link),
                                     parse_mode=ParseMode.HTML)
        except:
            pass
    update.effective_message.reply_text(strings.get(strings.admins_have_been_notified,chat))


handlers=[
    PrivateCommandHandler('ping',ping),
    GroupMessageHandler(Filters.regex(r'!\w+$'),macro),
    GroupCommandHandler('rules',rules),
    GroupMessageHandler(Filters.regex(r'@admin'),alert_admin)
]
