from telegram import Chat,Update
from const import CHAT_TO_LANGUAGE


def get(string,language,*args):
    if type(language)==Chat:
        language=CHAT_TO_LANGUAGE.get(language.id)
    elif type(language)==int:
        language=CHAT_TO_LANGUAGE.get(language)
    elif type(language)==Update:
        language=language.effective_user.language_code
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

reason={'en':'*Reason*: {}',
        'it':'*Motivo*: {}'}

user_has_been_warned={'en':'{} has been warned\n'
                           'Current warns: {}/{}',
                      'it':'{} è stato warnato\n'
                           'Warn attuali: {}/{}'}

operation_not_allowed={'en':'Operation not allowed during the current conversation',
                       'it':'Operazione non ammessa nella conversazione corrente'}

conversation_canceled={'en':'Conversation canceled',
                       'it':'Conversazione annullata'}

# @ADMIN
admins_have_been_notified={'en':'Admins have been notified',
                           'it':'Gli amministratori sono stati avvertiti'}

user_needs_help={'en':'{} needs <a href="{}">help</a>',
                 'it':'{} sta chiedendo <a href="{}">aiuto</a>'}

# SETUP
group_start_message={'en':'Thank you for adding me to this group. Make me an admin and '
                          'start me in private, then use /settings here to change the settings of the group',
                     'it':'Grazie per avermi aggiunto a questo gruppo. Rendimi admin e '
                          'startami in privato, poi usa /settings qui per cambiare le impostazioni del gruppo'}

private_start_message={
    'en':'Welcome in the Smart Group Guardian setting menu. '
         'Use /settings in a group to change its settings',
    'it':'Benvenuto nel menu impostazioni di Smart Group Guardian. '
         'Usa /settings in un gruppo per cambiarne le impostazioni'}

go_to_private={'en':'Go to our private chat to edit settings',
               'it':'Vai nella nostra chat privata per modificare le impostazioni'}

current_group={'en':'You are changing the settings for {}',
               'it':'Stai cambiando le impostazioni per {}'}

select_setting={'en':'Select the setting you want to change',
                'it':'Scegli l\'impostazione che vuoi cambiare'}

# SETUP BUTTONS
set_language_button={'en':'Language',
                     'it':'Lingua'}

choose_a_language={'en':'Choose a language',
                   'it':'Scegli una lingua'}

language_has_been_set={'en':'Language has been set',
                       'it':'La lingua è stata impostata'}

language_not_complete={'en':'Some contents may be not available in this language',  # IMPORTANT FOR NEW LANGUAGES
                       'it':'Alcuni contenuti potrebbero non essere disponibili in questa lingua'}

set_welcome_button={'en':'Welcome',
                    'it':'Benvenuto'}

ask_for_welcome_message={'en':'Send me the new welcome message for your group',
                         'it':'Mandami il nuovo messaggio di benvenuto per il tuo gruppo'}

welcome_message_has_been_set={'en':'The new welcome message has been set',
                              'it':'Il nuovo messaggio di benvenuto è stato impostato'}

set_rules_button={'en':'Rules',
                  'it':'Regole'}

ask_for_rules={'en':'Send me the new rules for your group',
               'it':'Mandami le nuove regole per il tuo gruppo'}

rules_have_been_set={'en':'The new rules have been set',
                     'it':'Le nuove regole sono state impostate'}

set_macros_button={'en':'Macros',
                   'it':'Macro'}

ask_for_macro_name={'en':'Send me the new macro\'s name',
                    'it':'Mandami il nome della nuova macro'}

ask_for_macro_content={'en':'Send me the new macro\'s content',
                       'it':'Mandami il contenuto della nuova macro'}

macro_has_been_set={'en':'The new macro has been set',
                    'it':'La nuova macro è stata impostata'}

set_warn_button={'en':'Warn',
                 'it':'Warn'}

ask_for_warn_limit={'en':'Send me the warn limit to set for your group',
                    'it':'Mandami il limite di warn da impostare per il tuo gruppo'}

ask_for_warn_limit_action={'en':'Send me the action to perform when the warn limit is reached',
                           'it':'Mandami l\'azione da fare quando il limite di warn viene raggiunto'}

warn_settings_have_been_set={'en':'The new warn settings have been set',
                             'it':'Le nuove impostazioni dei warn sono state impostate'}
