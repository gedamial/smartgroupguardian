from telegram import ChatMember


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
