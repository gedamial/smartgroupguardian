from telegram import ParseMode,ChatPermissions
import strings
from decorators import bot_admin,user_admin,target_not_admin,target_member,has_target,target_not_self,target_restricted
from utils import is_banned,GroupCommandHandler
from data_base import add_warn,get_warn,get_warn_limit,clear_warn,get_warn_limit_action


@bot_admin
@user_admin
@has_target
@target_not_self
@target_not_admin
def ban(update,context):  # TODO until_date, button to unban
    chat=update.effective_chat
    bot=context.bot
    user_to_ban=update.effective_message.reply_to_message.from_user
    reason=' '.join(context.args)  # FIXME when until_date is added as option
    bot.kick_chat_member(chat.id,user_to_ban.id)
    update.effective_message.reply_text(strings.get(strings.user_has_been_banned,chat,
                                                    user_to_ban.mention_html())+'\n'+
                                        (strings.get(strings.reason,chat,reason) if reason else ''),
                                        parse_mode=ParseMode.HTML)


@bot_admin
@user_admin
@has_target
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
                                                        user_to_unban.mention_html()),
                                            parse_mode=ParseMode.HTML)
    else:
        update.effective_message.reply_text(strings.get(strings.user_is_not_banned,chat,
                                                        user_to_unban.mention_html()),
                                            parse_mode=ParseMode.HTML)


@bot_admin
@user_admin
@has_target
@target_not_self
@target_not_admin
@target_member
def kick(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_kick=update.effective_message.reply_to_message.from_user
    reason=' '.join(context.args)
    if is_banned(user_to_kick.id,chat.id,bot):
        return update.effective_message.reply_text(strings.get(strings.user_is_not_member,chat,
                                                               user_to_kick.mention_html()),
                                                   parse_mode=ParseMode.HTML)
    bot.kick_chat_member(chat.id,user_to_kick.id)
    bot.unban_chat_member(chat.id,user_to_kick.id)
    update.effective_message.reply_text(strings.get(strings.user_has_been_kicked,chat,
                                                    user_to_kick.mention_html())+'\n'+
                                        (strings.get(strings.reason,chat,reason) if reason else ''),
                                        parse_mode=ParseMode.HTML)


@bot_admin
@user_admin
@has_target
@target_not_self
@target_not_admin
@target_member
def mute(update,context):  # TODO until_date, button to unmute
    chat=update.effective_chat
    bot=context.bot
    user_to_mute=update.effective_message.reply_to_message.from_user
    bot.restrict_chat_member(chat.id,user_to_mute.id,ChatPermissions(can_send_messages=False))
    update.effective_message.reply_text(strings.get(strings.user_has_been_muted,chat,
                                                    user_to_mute.mention_html()),
                                        parse_mode=ParseMode.HTML)


@bot_admin
@user_admin
@has_target
@target_not_self
@target_not_admin
@target_member
@target_restricted
def unmute(update,context):
    chat=update.effective_chat
    bot=context.bot
    user_to_unmute=update.effective_message.reply_to_message.from_user
    bot.restrict_chat_member(chat.id,user_to_unmute.id,bot.get_chat(chat.id).permissions)
    update.effective_message.reply_text(strings.get(strings.user_has_been_unmuted,chat,
                                                    user_to_unmute.mention_html()),
                                        parse_mode=ParseMode.HTML)


@bot_admin
@user_admin
@has_target
@target_not_self
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
                                                        user_to_warn.mention_html(),current_warn,warn_limit),
                                            parse_mode=ParseMode.HTML)
    else:
        clear_warn(user_to_warn.id,chat.id)
        action_to_perform=get_warn_limit_action(chat.id)
        # TODO perform the right action


handlers=[
    GroupCommandHandler('ban',ban),
    GroupCommandHandler('unban',unban),
    GroupCommandHandler('kick',kick),
    GroupCommandHandler('mute',mute),
    GroupCommandHandler('unmute',unmute),
    GroupCommandHandler('warn',warn)
]
