from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')
TOKEN=config['CONST']['TOKEN']

# TODO to use with DB to achieve persistence
# contains informations regarding the language for each chat: chat_id -> language_code
CHAT_TO_LANGUAGE=dict()  # =data_base.get_chat_languages()
LANGUAGES=[['ENGLISH','ITALIANO']]
COMPLETE_LANGUAGES=['ENGLISH']
LANGUAGE_CODES={'ITALIANO':'it','ENGLISH':'en'}
WARN_LIMIT_ACTIONS=[['BAN'],['MUTE'],['KICK']]  # to define
