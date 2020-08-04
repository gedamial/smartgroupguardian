# functions to use while configuring the bot for a group. to work in private, for admins only
from utils import PrivateCommandHandler,GroupCommandHandler


def start(update,context):
    # returns a button menu with the options to configure a group
    # like setting macros, setting welcome message ecc
    pass


def start_group(update,context):
    # should create a chat instance in the data base Chat(id,language_code,warn_limit,warn_limit_action,rules,...)
    pass


handlers=[
    PrivateCommandHandler('start',start),
    GroupCommandHandler('start',start_group)
]
