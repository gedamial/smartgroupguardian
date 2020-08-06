from telegram.ext import Updater
from const import TOKEN
from utils import error
import admins_only
import auto_triggered_functions
import public_functions
import setup_functions


def add_handlers(dispatcher,module):
    for handler in module.handlers:
        dispatcher.add_handler(handler)


def main():
    updater=Updater(TOKEN,use_context=True)
    dispatcher=updater.dispatcher
    dispatcher.add_error_handler(error)  # TODO only for testing
    add_handlers(dispatcher,admins_only)
    add_handlers(dispatcher,public_functions)
    add_handlers(dispatcher,setup_functions)
    
    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    main()
