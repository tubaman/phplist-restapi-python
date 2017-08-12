import unittest
from urllib.parse import urlsplit
from netrc import netrc

from phplist import PHPListClient, CommandNotFoundError


URL = "http://freebeerai.com/m/admin/?page=call&pi=restapi"


class TestLogin(unittest.TestCase):

    def test_login(self):
        domain = urlsplit(URL).netloc
        username, secret, password = netrc().authenticators(domain)
        client = PHPListClient(URL, secret=secret)
        output = client.login(login=username, password=password)
        self.assertEqual(output['type'], 'SystemMessage')


class TestAPICalls(unittest.TestCase):

    def setUp(self):
        domain = urlsplit(URL).netloc
        username, secret, password = netrc().authenticators(domain)
        self.client = PHPListClient(URL, secret=secret)
        self.client.login(login=username, password=password)

    def test_lists_get(self):
        output = self.client.lists_get()
        self.assertEqual(output['type'], 'Lists')

    def test_list_get(self):
        output = self.client.list_get(id=1)
        self.assertEqual(output['type'], 'List')

    def test_invalid_command_name(self):
        with self.assertRaises(CommandNotFoundError):
            output = self.client.foobar()
