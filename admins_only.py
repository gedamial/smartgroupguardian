from telegram.ext import CommandHandler,Filters
from telegram import ParseMode,ChatPermissions

import strings
from decorators import bot_admin,user_admin,target_not_admin,target_member
from utils import is_banned


@bot_admin
@user_admin
@target_not_admin
def ban(update,context):  # TODO until_date,reply_markup
    chat=update.effective_chat
    bot=context.bot
    user_to_ban=update.effective_message.reply_to_message.from_user
    reason=' '.join(update.effective_message.text.split()[1:])
    bot.kick_chat_member(chat.id,user_to_ban.id)
    update.effective_message.reply_text(strings.get(strings.user_has_been_banned,chat,user_to_ban.first_name)+
                                        ('\n'+strings.get(strings.reason,chat,reason) if reason else ''))


@bot_admin
@user_admin
def unban(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_unban=update.effective_message.reply_to_message.from_user
    if is_banned(user_to_unban.id,chat.id,bot):
        bot.unban_chat_member(chat.id,user_to_unban.id)
        try:
            bot.send_message(user_to_unban.id,strings.get(strings.you_can_join,user_to_unban.language_code,
                                                          f'<a href="https://t.me/{update.effective_chat.username}">{chat.title}</a>'),
                             parse_mode=ParseMode.HTML)
        except:
            pass
        update.effective_message.reply_text(strings.get(strings.user_has_been_unbanned,chat,user_to_unban.first_name))
    else:
        update.effective_message.reply_text(strings.get(strings.user_is_not_banned,chat,user_to_unban.first_name))


@bot_admin
@user_admin
@target_not_admin
@target_member
def kick(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_kick=update.effective_message.reply_to_message.from_user
    reason=' '.join(update.effective_message.text.split()[1:])
    if is_banned(user_to_kick.id,chat.id,bot):
        return update.effective_message.reply_text(strings.get(strings.user_is_not_member,chat,user_to_kick.first_name))
    bot.kick_chat_member(chat.id,user_to_kick.id)
    bot.unban_chat_member(chat.id,user_to_kick.id)
    update.effective_message.reply_text(strings.get(strings.user_has_been_kicked,chat,user_to_kick.first_name)+
                                        ('\n'+strings.get(strings.reason,chat,reason) if reason else ''))


@bot_admin
@user_admin
@target_not_admin
@target_member
def mute(update,context):  # TODO until_date
    chat=update.effective_chat
    bot=context.bot
    user_to_mute=update.effective_message.reply_to_message.from_user
    bot.restrict_chat_member(chat.id,user_to_mute.id,ChatPermissions(can_send_messages=False))
    update.effective_message.reply_text(strings.get(strings.user_has_been_muted,chat,user_to_mute.first_name))


@bot_admin
@user_admin
@target_not_admin
@target_member
def unmute(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_unmute=update.effective_message.reply_to_message.from_user
    bot.restrict_chat_member(chat.id,user_to_unmute.id,ChatPermissions(can_send_messages=True))
    update.effective_message.reply_text(strings.get(strings.user_has_been_unmuted,chat,user_to_unmute.first_name))


handlers=[
    CommandHandler('ban',ban,Filters.reply&Filters.group),
    CommandHandler('unban',unban,Filters.reply&Filters.group),
    CommandHandler('kick',kick,Filters.reply&Filters.group),
    CommandHandler('mute',mute,Filters.reply&Filters.group),
    CommandHandler('unmute',unmute,Filters.reply&Filters.group)
]
