from telegram import Update
from data_base import get_welcome_message, get_bad_words, add_suspicious_bad_word, add_warn
from difflib import SequenceMatcher
from threading import Thread
from sqlite3 import DatabaseError
from time import sleep


def welcome(update, context):
    # test to check if it's better to send one message per each user in message.new_chat_members or
    # one single message per update, since update.message.new_chat_members could contain many members
    welcome_message = get_welcome_message(update.effective_chat.id)
    if welcome_message:
        update.message.reply_text(welcome_message)

    #####   Bad Words #####
        
# this function's handlers should be added in a different group to let it run for each message
def bad_word(update: Update, context):
    Thread(bad_word_thread(update)).start()


def bad_word_thread(update: Update):
    words = update.message.text.split()
    # The While-Try-Except statement is used because multithreading could cause DB connection errors
    while True:
        try:
            bad_words = get_bad_words(update.message.chat_id)  # Get list of bad words from DB
            break
        except DatabaseError:
            sleep(1)
    for bad_word_ in bad_words:
        for word in words:
            if (bad_word_ == word) or (bad_word_ in [word[i:i + len(bad_word_)] for i in range(len(word))]):  # Checks if
                # the word equals the bad world or if contains it
                add_warn(update.effective_user.id, update.effective_chat.id)  # Warn User
                return
            elif SequenceMatcher(None, word, bad_word_).ratio() > 0.7:  # If the word is similar to a bad word / 0.7 value must be tested
                # The While-Try-Except statement is used because multithreading could cause DB connection errors
                while True:
                    try:
                        add_suspicious_bad_word(update.message.chat_id, word)  # Add word to suspicious-words Database
                        break
                    except DatabaseError:
                        sleep(1)

    #######################

handlers = [
    MessageHandler(Filters.status_update.new_chat_members, welcome)
]

