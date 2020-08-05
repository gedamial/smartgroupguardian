# functions to use while configuring the bot for a group. to work in private, for admins only
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import ConversationHandler,CallbackQueryHandler,Filters,MessageHandler
from const import LANGUAGES,LANGUAGE_CODES,COMPLETE_LANGUAGES,CHAT_TO_LANGUAGE
import strings
from data_base import set_admin_current_chat,set_chat_language,get_admin_current_chat
from decorators import bot_admin,user_admin,user_admin_in_current_chat,bot_admin_in_current_chat
from utils import PrivateCommandHandler,GroupCommandHandler,generic_fallback_handler,cancel_handler


def start(update,context):
    update.effective_message.reply_text(strings.get(strings.private_start_message,update.effective_chat))


def start_group(update,context):
    # should create a chat instance in the data base Chat(id,language_code,warn_limit,warn_limit_action,rules,...)
    update.effective_message.reply_text(strings.get(strings.group_start_message,update.effective_chat))


def create_settings_keyboard(language):  # TODO
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(strings.get(strings.set_language,language),callback_data='set_language'),
            InlineKeyboardButton(strings.get(strings.set_welcome,language),callback_data='set_welcome')
        ],
        [
            InlineKeyboardButton(strings.get(strings.set_rules,language),callback_data='set_rules'),
            InlineKeyboardButton(strings.get(strings.set_macros,language),callback_data='set_macros')
        ],
        [
            InlineKeyboardButton(strings.get(strings.set_warn,language),callback_data='set_warn')
        ]
    ])


@bot_admin
@user_admin
def settings(update,context):
    user=update.effective_user
    chat=update.effective_chat
    bot=context.bot
    set_admin_current_chat(user.id)
    update.effective_message.reply_text(strings.get(strings.go_to_private,chat))
    bot.send_message(user.id,strings.get(strings.current_group,user.language_code,
                                         chat.title))
    bot.send_message(user.id,strings.get(strings.select_setting,user.language_code),
                     reply_markup=create_settings_keyboard(user.language_code))


WAITING_FOR_LANGUAGE=0


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_set_language_button_pressed(update,context):
    update.effective_message.reply_text(strings.get(strings.choose_a_language,update),
                                        reply_markup=ReplyKeyboardMarkup(LANGUAGES))
    return WAITING_FOR_LANGUAGE


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_language_received(update,context):
    current_chat=get_admin_current_chat(update.effective_user.id)
    set_chat_language(current_chat,LANGUAGE_CODES[update.effective_message.text])
    CHAT_TO_LANGUAGE[current_chat]=LANGUAGE_CODES[update.effective_message.text]
    update.effective_message.reply_text(strings.get(strings.language_was_set,update),
                                        reply_markup=ReplyKeyboardRemove())
    if update.effective_message.text not in COMPLETE_LANGUAGES:
        update.effective_message.reply_text(strings.get(strings.language_not_complete,update))
    return ConversationHandler.END


set_language_conversation=ConversationHandler(
    entry_points=[CallbackQueryHandler(on_set_language_button_pressed,pattern='set_language')],
    states={
        WAITING_FOR_LANGUAGE:[MessageHandler(Filters.regex(rf'^{"|".join(sum(LANGUAGES,[]))}$'),on_language_received)]
    },
    fallbacks=[cancel_handler,generic_fallback_handler]
)

handlers=[
    PrivateCommandHandler('start',start),
    GroupCommandHandler('start',start_group),
    GroupCommandHandler('settings',settings),
    set_language_conversation
]
