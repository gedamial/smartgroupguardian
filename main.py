from telegram.ext import Updater

from const import TOKEN
import admins_only


def add_handlers(dispatcher,module):
    for handler in module.handlers:
        dispatcher.add_handler(handler)


def main():
    updater=Updater(TOKEN,use_context=True)
    dispatcher=updater.dispatcher
    
    add_handlers(dispatcher,admins_only)
    
    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    main()
