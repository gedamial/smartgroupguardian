from telegram import Chat
from const import CHAT_TO_LOANGUAGE


def get(string,language,*args):
    if type(language)==Chat:
        language=CHAT_TO_LOANGUAGE.get(language.id)
    elif type(language)==int:
        language=CHAT_TO_LOANGUAGE.get(language)
    return string.get(language,string['en']).format(*args)


ping_success={'en':'PING SUCCESS',
              'it':'PING RIUSCITO'}

generic_error={'en':'An error occurred during the execution of the command',
               'it':'Si è verificato un errore durante l\'esecuzione del comando'}

am_i_admin={'en':'Am I admin?',
            'it':'Sono admin?'}

cannot_perform_on_admin={'en':'Cannot perform this action on another admin',
                         'it':'Non posso eseguire questa azione su un altro admin'}

you_can_join={'en':'You can join the group chat again {}',
              'it':'Ora puoi tornare nel gruppo {}'}

user_is_not_banned={'en':'{} is not banned',
                    'it':'{} non è bannato'}

user_has_been_banned={'en':'{} has been banned',
                      'it':'{} è stato bannato'}

user_has_been_unbanned={'en':'{} has been unbanned',
                        'it':'{} è stato sbannato'}

user_has_been_kicked={'en':'{} has been kicked',
                      'it':'{} è stato kickato'}

user_has_been_muted={'en':'{} has been muted',
                     'it':'{} è stato mutato'}

user_has_been_unmuted={'en':'{} has been unmuted'}

user_is_not_member={'en':'{} is not a member of this group',
                    'it':'{} non fa parte della chat'}

reason={'en':'Reason: {}',
        'it':'Motivo: {}'}
