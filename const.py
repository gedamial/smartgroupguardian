from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')
TOKEN=config['CONST']['TOKEN']

# TODO to use with DB to achieve persistence
CHAT_TO_LOANGUAGE=dict()  # contains informations regarding the language for each chat: chat_id -> language_code
