from telegram import ChatMember,ReplyKeyboardRemove,ChatPermissions
from telegram.ext import MessageHandler,Filters,CommandHandler,ConversationHandler
import strings
from traceback import format_exception


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


def is_restricted(user_id,chat_id,bot):
    try:
        chat_permissions=bot.get_chat(chat_id).permissions
        user=bot.get_chat_member(chat_id,user_id)
        user_permissions=ChatPermissions(can_send_messages=user.can_send_messages,
                                         can_send_media_messages=user.can_send_media_messages,
                                         can_send_polls=user.can_send_polls,
                                         can_send_other_messages=user.can_send_other_messages,
                                         can_add_web_page_previews=user.can_add_web_page_previews,
                                         can_change_info=user.can_change_info,
                                         can_invite_users=user.can_invite_users,
                                         can_pin_messages=user.can_pin_messages)
        return user_permissions!=chat_permissions
    except:
        return False


def generic_fallback(update,context):
    update.effective_message.reply_text(strings.get(strings.operation_not_allowed,update))


def cancel(udpate,context):
    udpate.effective_message.reply_text(strings.get(strings.conversation_canceled,udpate),
                                        reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


generic_fallback_handler=MessageHandler(Filters.all,generic_fallback)
cancel_handler=CommandHandler('cancel',cancel)


def error(update,context):  # TODO only for testing
    update.effective_message.reply_text(''.join(format_exception(None,context.error,context.error.__traceback__)))
