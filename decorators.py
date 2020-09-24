import strings
from utils import am_i_admin,is_admin,is_member,is_restricted
from data_base import get_admin_current_chat,get_night_mode
from datetime import datetime, timedelta, date

def night_mode(func):
    def wrapper(update, context):
        from_time_setting, minutes = get_night_mode(update.effective_chat.id) # get chat night mode settings
        if (from_time_setting is None or minutes is None): # check night mode settings
            return func(update, context) # this means that there is no night mode set for the chat and therefore you can go
        
        # if you are here it means that there is a night mode set for the chat
        from_time = datetime.combine(date.today(), from_time_setting) # get the starting time of the night mode
        to_time = timedelta(minutes = minutes) + from_time # get the ending time of the night mode by adding the minutes
        
        if (am_i_admin(context.bot, update.effective_chat.id) or not(from_time <= datetime.now() <= to_time)): # if you are an admin or you are not in between the night time hours
            return func(update, context) # you can safely go cause you are either an admin or not in night mode
        context.bot.delete_message(update.effective_chat.id,update.effective_message.message_id) # or else your message will be deleted
                                   
    return wrapper

def bot_admin(func):
    def wrapper(update,context):
        if am_i_admin(context.bot,update.effective_chat.id):
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.am_i_admin,update.effective_chat))
    
    return wrapper


def bot_admin_in_current_chat(func):
    def wrapper(update,context):
        if am_i_admin(context.bot,get_admin_current_chat(update.effective_user.id)):
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.am_i_admin,update.effective_chat))
    
    return wrapper


def user_admin(func):
    def wrapper(update,context):
        if is_admin(update.effective_user.id,update.effective_chat.id,context.bot):
            return func(update,context)
        context.bot.delete_message(update.effective_chat.id,update.effective_message.message_id)
    
    return wrapper


def user_admin_in_current_chat(func):
    def wrapper(update,context):
        user_id=update.effective_user.id
        if is_admin(user_id,get_admin_current_chat(user_id),context.bot):
            return func(update,context)
    
    return wrapper


def has_target(func):
    def wrapper(update,context):
        if update.effective_message.reply_to_message:
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.this_command_needs_target,update.effective_chat))
    
    return wrapper


def target_not_self(func):
    def wrapper(update,context):
        target_id=update.effective_message.reply_to_message.from_user.id
        user_id=update.effective_message.from_user.id
        bot_id=context.bot.get_me().id
        if target_id not in (user_id,bot_id):
            return func(update,context)
        if target_id==user_id:
            update.effective_message.reply_text(strings.get(strings.cannot_perform_on_you,update.effective_chat))
        elif target_id==bot_id:
            update.effective_message.reply_text(strings.get(strings.cannot_perform_on_me,update.effective_chat))
    
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


def target_restricted(func):
    def wrapper(update,context):
        if is_restricted(update.effective_message.reply_to_message.from_user.id,update.effective_chat.id,context.bot):
            return func(update,context)
        update.effective_message.reply_text(strings.get(strings.user_is_not_restricted,update.effective_chat,
                                                        update.effective_message.reply_to_message.from_user.first_name))
    
    return wrapper
