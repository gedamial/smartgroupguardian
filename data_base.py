# TODO connection using values from config.ini
# TODO functions should return None in case of missing data
def get_chat_languages():  # returns a dict: chat_data -> language_code
    pass


# CHAT SETUP
def create_chat():  # should take several arguments to define
    pass


def set_admin_current_chat(user_id):  # sets the id of the group set by the admin using /settings
    pass


def get_admin_current_chat(user_id):  # returns the id of the group set by the admin using /settings
    pass


def set_chat_language(chat_id,language_code):
    pass


# WELCOME MESSAGE
def set_welcome_message(chat_id,welcome_message):  # sets welcome_message as the welcome message for the requested chat
    pass


def get_welcome_message(chat_id):  # returns the welcome message for the requested chat
    pass


# RULES
def set_rules(chat_id,rules):
    pass


def get_rules(chat_id):
    pass


# MACRO
def set_macro(chat_id,macro_name,macro_content):  # sets the content for the requested macro in the requested chat
    pass


def get_macro(chat_id,macro_name):  # returns the content of the requested macro for the requested chat
    pass


# WARN
# THESE FUNCTIONS SHOULD NEVER RETURN A NON-INTEGER VALUE
def add_warn(user_id,chat_id):  # creates the user and sets count to 1 if not warned yet
    pass


def remove_warn(user_id,chat_id):  # removes 1 warn for the requested user in the requested chat
    pass


def clear_warn(user_id,chat_id):
    set_warn(user_id,chat_id,0)


def set_warn(user_id,chat_id,value):
    pass


def get_warn(user_id,chat_id):  # creates the user and sets the warn count to 0 if not warned yet
    pass


def set_warn_limit(chat_id,value):  # sets the warn limit for the requested chat
    pass


def get_warn_limit(chat_id):  # returns the warn limit for the requested chat
    pass


def set_warn_limit_action(chat_id,action):
    # sets the action to perform when the chat's warn limit is reached for a user (ban, kick, mute)
    pass


def get_warn_limit_action(chat_id):
    pass
