from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')
TOKEN=config['CONST']['TOKEN']

# TODO to use with DB to achieve persistence
# contains informations regarding the language for each chat: chat_id -> language_code
CHAT_TO_LANGUAGE=dict()  # =data_base.get_chat_languages()
