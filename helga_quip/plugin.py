import re, requests
from helga.db import db
from helga.plugins import command, match, random_ack

_help_text = 'Match quips and other witticisms. Usage:\
1. helga quip phrase add/remove <quip_id> <quip_regex>\
2. helga quip kind add/remove <quip_id> <quip_phrase>'

def _quip_manage(client, channel, nick, message, args):
    """ Add/remove quip/phrase to stash """
    final = ' '.join(args[3:])
    if args[0] == 'kind':
        kind = {'kind':args[2], 'phrase':final}
        if args[1] == 'add':
            db.helga_quip.kind.insert(kind)
        elif args[1] == 'remove':
            db.helga_quip.kind.remove(kind)
    elif args[0] == 'phrase':
        phrase = {'kind':args[2], 'regex':final}
        if args[1] == 'add':
            phrase['nick'] = nick
            db.helga_quip.phrases.insert(phrase)
        elif args[1] == 'remove':
            db.helga_quip.phrases.remove(phrase)
    return random_ack()

def _quip_respond(message):
    """ Search for matching quip, respond if exists """
    for phrase in db.helga_quip.phrases.find():
        result = re.match(phrase['regex'], message)
        if result:
            kind = db.helga_quip.kind.find_one({'kind':phrase['kind']})
            return ('success', kind['phrase'] + ': ' + result.string)
    return ''

@match(_quip_respond)
@command('quip', aliases=['joke', 'quips'], help=_help_text)
def quip(client, channel, nick, message, *args):
    """ Helga endpoint for plugin """
    # hacky because this could be either match which already populated args or
    # regular command, which we need to process. surely theres a cleaner way.
    if len(args) == 2 and isinstance(args[1], (list,)):
        return _quip_manage(client, channel, nick, message, args[1])
    if args[0][0] == 'success':
        return args[0][1]

