from telegram.ext import Filters
from telegram import ParseMode,ChatPermissions
from telegram.utils.helpers import escape_markdown
import strings
from decorators import bot_admin,user_admin,target_not_admin,target_member
from utils import is_banned,GroupCommandHandler
from data_base import add_warn,get_warn,get_warn_limit,clear_warn,get_warn_limit_action


@bot_admin
@user_admin
@target_not_admin
def ban(update,context):  # TODO until_date, button to unban
    chat=update.effective_chat
    bot=context.bot
    user_to_ban=update.effective_message.reply_to_message.from_user
    reason=' '.join(context.args)  # FIXME when until_date is added as option
    bot.kick_chat_member(chat.id,user_to_ban.id)
    update.effective_message.reply_text(strings.get(strings.user_has_been_banned,chat,
                                                    escape_markdown(user_to_ban.first_name,version=2))+
                                        ('\n'+strings.get(strings.reason,chat,reason) if reason else ''),
                                        parse_mode=ParseMode.MARKDOWN_V2)


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
        update.effective_message.reply_text(strings.get(strings.user_has_been_unbanned,chat,
                                                        user_to_unban.first_name))
    else:
        update.effective_message.reply_text(strings.get(strings.user_is_not_banned,chat,
                                                        user_to_unban.first_name))


@bot_admin
@user_admin
@target_not_admin
@target_member
def kick(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_kick=update.effective_message.reply_to_message.from_user
    reason=' '.join(context.args)
    if is_banned(user_to_kick.id,chat.id,bot):
        return update.effective_message.reply_text(strings.get(strings.user_is_not_member,chat,
                                                               user_to_kick.first_name))
    bot.kick_chat_member(chat.id,user_to_kick.id)
    bot.unban_chat_member(chat.id,user_to_kick.id)
    update.effective_message.reply_text(strings.get(strings.user_has_been_kicked,chat,
                                                    escape_markdown(user_to_kick.first_name,version=2))+
                                        ('\n'+strings.get(strings.reason,chat,reason) if reason else ''),
                                        parse_mode=ParseMode.MARKDOWN_V2)


@bot_admin
@user_admin
@target_not_admin
@target_member
def mute(update,context):  # TODO until_date, button to unmute
    chat=update.effective_chat
    bot=context.bot
    user_to_mute=update.effective_message.reply_to_message.from_user
    bot.restrict_chat_member(chat.id,user_to_mute.id,ChatPermissions(can_send_messages=False))
    update.effective_message.reply_text(strings.get(strings.user_has_been_muted,chat,
                                                    user_to_mute.first_name))


@bot_admin
@user_admin
@target_not_admin
@target_member
def unmute(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_unmute=update.effective_message.reply_to_message.from_user
    bot.restrict_chat_member(chat.id,user_to_unmute.id,ChatPermissions(can_send_messages=True,
                                                                       can_send_media_messages=True,
                                                                       can_send_polls=True,
                                                                       can_send_other_messages=True,
                                                                       can_add_web_page_previews=True))
    update.effective_message.reply_text(strings.get(strings.user_has_been_unmuted,chat,
                                                    user_to_unmute.first_name))


@bot_admin
@user_admin
@target_not_admin
@target_member  # not actually needed to execute the command
def warn(update,context):  # TODO buttons to add and remove warns
    chat=update.effective_chat
    user_to_warn=update.effective_message.reply_to_message.from_user
    add_warn(user_to_warn.id,chat.id)
    current_warn=get_warn(user_to_warn.id,chat.id)
    warn_limit=get_warn_limit(chat.id)
    if current_warn<warn_limit:
        update.effective_message.reply_text(strings.get(strings.user_has_been_warned,chat,
                                                        user_to_warn.first_name,current_warn,warn_limit))
    else:
        clear_warn(user_to_warn.id,chat.id)
        action_to_perform=get_warn_limit_action(chat.id)
        # TODO perform the right action


handlers=[
    GroupCommandHandler('ban',ban,Filters.reply),
    GroupCommandHandler('unban',unban,Filters.reply),
    GroupCommandHandler('kick',kick,Filters.reply),
    GroupCommandHandler('mute',mute,Filters.reply),
    GroupCommandHandler('unmute',unmute,Filters.reply),
    GroupCommandHandler('warn',warn)
]
