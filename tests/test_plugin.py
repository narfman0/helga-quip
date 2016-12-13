import sys
from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    from mock import mock
from mongomock import MongoClient
sys.modules['helga.plugins'] = mock.Mock()
from helga.db import db


class TestResults(TestCase):
    def setUp(self):
        self.db_patch = mock.patch(
            'pymongo.MongoClient',
            new_callable=lambda: MongoClient
        )
        self.db_patch.start()
        self.addCleanup(self.db_patch.stop)

        from helga_quip import plugin
        self.plugin = plugin

    def tearDown(self):
        db.helga_quip.entries.delete_many({})

    def test_response_simple(self):
        quip = {
            'kind': 'response',
            'regex': 'message',
        }
        db.helga_quip.entries.insert(quip)
        success, response = self.plugin._quip_respond('message')
        self.assertEqual(response, quip['kind'])
        self.assertEqual(success, 'success')

    def test_response_named_backreference(self):
        quip = {
            'kind': '{action}',
            'regex': '(?P<action>despair|love) for life',
        }
        db.helga_quip.entries.insert(quip)

        success, response = self.plugin._quip_respond('despair for life')
        self.assertEqual(response, 'despair')
        success, response = self.plugin._quip_respond('love for life')
        self.assertEqual(response, 'love')
        response = self.plugin._quip_respond('ambivalence for life')
        self.assertEqual(response, None)

    def test_response_positional_backreference(self):
        quip = {
            'kind': 'your mom {0} really {1}',
            'regex': '(looks|is) really (leet|fat|awesome)',
        }
        db.helga_quip.entries.insert(quip)
        success, response = self.plugin._quip_respond('is really leet')
        self.assertEqual(response, 'your mom is really leet')

    def test_response_multiple(self):
        db.helga_quip.entries.insert_one({'kind': 'kind1', 'regex': 'regex1'})
        db.helga_quip.entries.insert_one({'kind': 'kind2', 'regex': 'regex1'})
        with mock.patch('helga_quip.plugin.choice', side_effect=lambda b: b[0]):
            success, response = self.plugin._quip_respond('regex1')
            self.assertEqual(response, 'kind1')
        with mock.patch('helga_quip.plugin.choice', side_effect=lambda b: b[1]):
            success, response = self.plugin._quip_respond('regex1')
            self.assertEqual(response, 'kind2')
