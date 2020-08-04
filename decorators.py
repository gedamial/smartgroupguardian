import strings
from utils import am_i_admin,is_admin,is_member


def bot_admin(func):
    def wrapper(update,context):
        if am_i_admin(context.bot,update.effective_chat.id):
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.am_i_admin,update.effective_chat))
    
    return wrapper


def user_admin(func):
    def wrapper(update,context):
        if is_admin(update.effective_user.id,update.effective_chat.id,context.bot):
            return func(update,context)
        context.bot.delete_message(update.effective_chat.id,update.effective_message.message_id)
    
    return wrapper


def target_not_admin(func):
    def wrapper(update,context):
        if not is_admin(update.effective_message.reply_to_message.from_user.id,update.effective_chat.id,context.bot):
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.cannot_perform_on_admin,update.effective_chat))
    
    return wrapper


def target_member(func):
    def wrapper(update,context):
        if is_member(update.effective_message.reply_to_message.from_user.id,update.effective_chat.id,context.bot):
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.user_is_not_member,update.effective_chat,
                                                        update.effective_message.reply_to_message.from_user.first_name))
    
    return wrapper
