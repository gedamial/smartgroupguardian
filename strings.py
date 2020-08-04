from telegram import Chat
from const import CHAT_TO_LANGUAGE


def get(string,language,*args):
    if type(language)==Chat:
        language=CHAT_TO_LANGUAGE.get(language.id)
    elif type(language)==int:
        language=CHAT_TO_LANGUAGE.get(language)
    return string.get(language,string['en']).format(*args)


ping_success={'en':'PING SUCCESS',
              'it':'PING RIUSCITO'}
# ERRORS
generic_error={'en':'An error occurred during the execution of the command',
               'it':'Si è verificato un errore durante l\'esecuzione del comando'}

am_i_admin={'en':'Am I admin?',
            'it':'Sono admin?'}

cannot_perform_on_admin={'en':'Cannot perform this action on another admin',
                         'it':'Non posso eseguire questa azione su un altro admin'}

user_is_not_banned={'en':'{} is not banned',
                    'it':'{} non è bannato'}

user_is_not_member={'en':'{} is not a member of this group',
                    'it':'{} non fa parte della chat'}

# REPLIES
you_can_join={'en':'You can join the group chat again {}',
              'it':'Ora puoi tornare nel gruppo {}'}

user_has_been_banned={'en':'{} has been banned',
                      'it':'{} è stato bannato'}

user_has_been_unbanned={'en':'{} has been unbanned',
                        'it':'{} è stato sbannato'}

user_has_been_kicked={'en':'{} has been kicked',
                      'it':'{} è stato kickato'}

user_has_been_muted={'en':'{} has been muted',
                     'it':'{} è stato mutato'}

user_has_been_unmuted={'en':'{} has been unmuted',
                       'it':'{} è stato smutato'}

reason={'en':'Reason: {}',
        'it':'Motivo: {}'}

user_has_been_warned={'en':'{} has been warned\n'
                           'Current warns: {}/{}'}

private_start_message={
    'en':'Welcome in the Smart Group Guardian setting menu. Forward a message from your group to start',
    'it':'Benvenuto nel menu impostazioni di Smart Group Guardian. Inoltra un messaggio dal tuo gruppo per iniziare'}

# @ADMIN
admins_have_been_notified={'en':'Admins have been notified',
                           'it':'Gli amministratori sono stati avvertiti'}

user_needs_help={'en':'{} needs <a href="{}">help</a>',
                 'it':'{} sta chiedendo <a href="{}">aiuto</a>'}
