# functions to use while configuring the bot for a group. to work in private, for admins only
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import ConversationHandler,CallbackQueryHandler,Filters,MessageHandler
from const import LANGUAGES,LANGUAGE_CODES,COMPLETE_LANGUAGES,CHAT_TO_LANGUAGE,WARN_LIMIT_ACTIONS
import strings
from data_base import set_admin_current_chat,set_chat_language,get_admin_current_chat,set_welcome_message,set_rules,\
    set_warn_limit,set_warn_limit_action,set_macro
from decorators import bot_admin,user_admin,user_admin_in_current_chat,bot_admin_in_current_chat
from utils import PrivateCommandHandler,GroupCommandHandler,generic_fallback_handler,cancel_handler


def start(update,context):
    update.effective_message.reply_text(strings.get(strings.private_start_message,update.effective_chat))


def start_group(update,context):
    # should create a chat instance in the data base Chat(id,language_code,warn_limit,warn_limit_action,rules,...)
    update.effective_message.reply_text(strings.get(strings.group_start_message,update.effective_chat))


def create_settings_keyboard(language):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(strings.get(strings.set_language_button,language),callback_data='set_language'),
            InlineKeyboardButton(strings.get(strings.set_welcome_button,language),callback_data='set_welcome')
        ],
        [
            InlineKeyboardButton(strings.get(strings.set_rules_button,language),callback_data='set_rules'),
            InlineKeyboardButton(strings.get(strings.set_macros_button,language),callback_data='set_macros')
        ],
        [
            InlineKeyboardButton(strings.get(strings.set_warn_button,language),callback_data='set_warn')
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


# SET LANGUAGE CONVERSATION
WAITING_FOR_LANGUAGE=0


# @bot_admin_in_current_chat  # don't work without data base
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
    update.effective_message.reply_text(strings.get(strings.language_has_been_set,update),
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

# SET WELCOME MESSAGE CONVERSATION
WAITING_FOR_WELCOME_MESSAGE=0


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_set_welcome_button_pressed(update,context):
    update.effective_message.reply_text(strings.get(strings.ask_for_welcome_message,update))
    return WAITING_FOR_WELCOME_MESSAGE


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_welcome_message_received(update,context):
    set_welcome_message(get_admin_current_chat(update.effective_user.id),update.effective_message.text)
    update.effective_message.reply_text(strings.get(strings.welcome_message_has_been_set,update))
    return ConversationHandler.END


set_welcome_conversation=ConversationHandler(
    entry_points=[CallbackQueryHandler(on_set_welcome_button_pressed,pattern='set_welcome')],
    states={
        WAITING_FOR_WELCOME_MESSAGE:[MessageHandler(Filters.text,on_welcome_message_received)]
    },
    fallbacks=[cancel_handler,generic_fallback_handler]
)

# SET RULES CONVERSATION
WAITING_FOR_RULES=0


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_set_rules_button_pressed(update,context):
    update.effective_message.reply_text(strings.get(strings.ask_for_rules,update))
    return WAITING_FOR_RULES


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_rules_received(update,context):
    set_rules(get_admin_current_chat(update.effective_user.id),update.effective_message.text)
    update.effective_message.reply_text(strings.get(strings.rules_have_been_set,update))
    return ConversationHandler.END


set_rules_conversation=ConversationHandler(
    entry_points=[CallbackQueryHandler(on_set_rules_button_pressed,pattern='set_rules')],
    states={
        WAITING_FOR_RULES:[MessageHandler(Filters.text,on_rules_received)]
    },
    fallbacks=[cancel_handler,generic_fallback_handler]
)

# SET MACROS CONVERSATION
WAITING_FOR_MACRO_NAME,WAITING_FOR_MACRO_CONTENT=0,1


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_set_macro_button_pressed(update,context):
    update.effective_message.reply_text(strings.get(strings.ask_for_macro_name,update))
    return WAITING_FOR_MACRO_NAME


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_macro_name_received(update,context):
    context.user_data['macro_name']=update.effective_message.text
    update.effective_message.reply_text(strings.get(strings.ask_for_macro_content,update))
    return WAITING_FOR_MACRO_CONTENT


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_macro_content_received(update,context):
    set_macro(get_admin_current_chat(
        update.effective_user.id),context.user_data['macro_name'],update.effective_message.text
    )
    update.effective_message.reply_text(strings.get(strings.macro_has_been_set,update))
    return ConversationHandler.END


set_macro_conversation=ConversationHandler(
    entry_points=[CallbackQueryHandler(on_set_macro_button_pressed,pattern='set_macro')],
    states={
        WAITING_FOR_MACRO_NAME:[MessageHandler(Filters.text,on_macro_name_received)],
        WAITING_FOR_MACRO_CONTENT:[MessageHandler(Filters.text,on_macro_content_received)]
    },
    fallbacks=[cancel_handler,generic_fallback_handler]
)

# SET WARN CONVERSATION
WAITING_FOR_WARN_LIMIT,WAITING_FOR_WARN_LIMIT_ACTION=0,1


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_set_warn_button_pressed(update,context):
    update.effective_message.reply_text(strings.get(strings.ask_for_warn_limit,update))
    return WAITING_FOR_WARN_LIMIT


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_warn_limit_received(update,context):
    set_warn_limit(get_admin_current_chat(update.effective_user.id),int(update.effective_message.text))
    update.effective_message.reply_text(strings.get(strings.ask_for_warn_limit_action,update),
                                        reply_markup=ReplyKeyboardMarkup(WARN_LIMIT_ACTIONS))
    return WAITING_FOR_WARN_LIMIT_ACTION


# @bot_admin_in_current_chat
# @user_admin_in_current_chat
def on_warn_limit_action_received(update,context):
    set_warn_limit_action(get_admin_current_chat(update.effective_user.id),update.effective_message.text)
    update.effective_message.reply_text(strings.get(strings.warn_settings_have_been_set,update),
                                        reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


set_warn_conversation=ConversationHandler(
    entry_points=[CallbackQueryHandler(on_set_warn_button_pressed,pattern='set_warn')],
    states={
        WAITING_FOR_WARN_LIMIT:[MessageHandler(Filters.regex(r'^\d+$'),on_warn_limit_received)],
        WAITING_FOR_WARN_LIMIT_ACTION:[
            MessageHandler(Filters.regex(rf'^{"|".join(sum(WARN_LIMIT_ACTIONS,[]))}$'),on_warn_limit_action_received)
        ]
    },
    fallbacks=[cancel_handler,generic_fallback_handler]
)

handlers=[
    PrivateCommandHandler('start',start),
    GroupCommandHandler('start',start_group),
    GroupCommandHandler('settings',settings),
    set_language_conversation,
    set_welcome_conversation,
    set_rules_conversation,
    set_macro_conversation,
    set_warn_conversation
]
