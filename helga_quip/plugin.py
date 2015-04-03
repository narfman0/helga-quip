""" Helga entry point for plugin """
import re, requests
from helga.db import db
from helga.plugins import command, match, random_ack

_help_text = 'Match quips and other witticisms. Usage:\
!quip add/remove <quip_kind> <quip_regex>\
Example:\
1. !quip add "thats what she said" "(it|that|this) (sounds|is|was) really hard"\
2. !quip add "your mom {0}" "(looks|is) really (leet|fat|awesome)"'

def _quip_manage(client, channel, nick, message, args):
    """ Add/remove quip/phrase to stash """
    if args[0] == 'drop':
        db.helga_quip.entries.drop()
    elif args[0] == 'dump':
        quips = [p['regex'] + ' | ' + p['kind'] for p in db.helga_quip.entries.find()]
        payload = {'title':'helga-quip dump', 'content': '\n'.join(quips)}
        r = requests.post("http://dpaste.com/api/v2/", payload)
        return r.headers['location']
    else:
        phrase = {'kind':args[1], 'regex':args[2]}
        if args[0] == 'add':
            phrase['nick'] = nick
            try:
                re.compile(phrase['regex'])
            except:
                return 'Invalid regex: %s' % phrase['regex']
            db.helga_quip.entries.insert(phrase)
        elif args[0] == 'remove':
            db.helga_quip.entries.remove(phrase)
    return random_ack()

def _quip_respond(message):
    """ Search for matching quip, respond if exists """
    for phrase in db.helga_quip.entries.find():
        result = re.search(phrase['regex'], message, re.I)
        if result:
            quip = phrase['kind']
            if '{0}' in quip:
                quip = quip.format(result.group(0))
            return ('success', quip)

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
