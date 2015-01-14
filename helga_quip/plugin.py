import re
from helga.db import db
from helga.plugins import command, match, random_ack

_help_text = 'Match quips and other witticisms. Usage:\
1. helga quip add/remove <quip_kind> <quip_regex>'

def _quip_manage(client, channel, nick, message, args):
    """ Add/remove quip/phrase to stash """
    regex = '.*' + args[2] + '.*'
    phrase = {'kind':args[1], 'regex':regex}
    if args[0] == 'add':
        phrase['nick'] = nick
        db.helga_quip.entries.insert(phrase)
    elif args[0] == 'remove':
        db.helga_quip.entries.remove(phrase)
    return random_ack()

def _quip_respond(message):
    """ Search for matching quip, respond if exists """
    for phrase in db.helga_quip.entries.find():
        result = re.match(phrase['regex'], message)
        if result:
            return ('success', phrase['kind'])
    return ''

@match(_quip_respond)
@command('quip', aliases=['joke', 'quips'], help=_help_text, shlex=True)
def quip(client, channel, nick, message, *args):
    """ Helga endpoint for plugin """
    # hacky because this could be either match which already populated args or
    # regular command, which we need to process. surely theres a cleaner way.
    if len(args) == 2 and isinstance(args[1], (list,)):
        return _quip_manage(client, channel, nick, message, args[1])
    if args[0][0] == 'success':
        return args[0][1]
