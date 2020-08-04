from telegram import ChatMember
from telegram.ext import MessageHandler,Filters,CommandHandler


class RegexCommandHandler(MessageHandler):
    def __init__(self,command_pattern,callback,filters=Filters.all):
        super().__init__(filters&Filters.regex(rf'^/{command_pattern}\b'),callback)


class GroupMessageHandler(MessageHandler):
    def __init__(self,filters,callback):
        super().__init__(filters&Filters.group,callback)


class GroupCommandHandler(CommandHandler):
    def __init__(self,command,callback,filters=Filters.all):
        super().__init__(command,callback,filters&Filters.group)


class PrivateMessageHandler(MessageHandler):
    def __init__(self,filters,callback):
        super().__init__(filters&Filters.private,callback)


class PrivateCommandHandler(CommandHandler):
    def __init__(self,command,callback,filters=Filters.all):
        super().__init__(command,callback,filters&Filters.private)


def is_admin(user_id,chat_id,bot):
    return user_id in map(lambda x:x.user.id,bot.get_chat_administrators(chat_id))


def am_i_admin(bot,chat_id):
    return is_admin(bot.get_me().id,chat_id,bot)


def is_banned(user_id,chat_id,bot):
    return bot.get_chat_member(chat_id,user_id).status==ChatMember.KICKED


def is_member(user_id,chat_id,bot):
    try:
        return bot.get_chat_member(chat_id,user_id).status not in (ChatMember.KICKED,ChatMember.LEFT)
    except:
        return False


def error(update,context):  # TODO only for testing
    update.effective_message.reply_text(str(context.error))
