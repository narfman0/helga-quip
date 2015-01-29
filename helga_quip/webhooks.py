""" Webhook for quips displaying all current quips for management """
from helga.db import db
from helga.plugins.webhooks import route

@route(r'/helga-quip')
def quip_route(request, client):
    """ Return table of current entries in quip for easy remove/manipulate"""
    # Consider using templated logic/presentation splitter e.g. mustache. So
    # trivial though, and so much code to write in this world.
    response = '<table><tr><th>Regex</th><th>Response</th></tr>'
    for phrase in db.helga_quip.entries.find():
        response += ('<tr><td>' + phrase['regex'] + '</td><td>' +
                     phrase['kind'] + '</tr>')
    return response + '</table>'
