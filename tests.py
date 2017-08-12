import unittest
from urllib.parse import urlsplit
from netrc import netrc

from phplist import PHPListClient


URL = "http://freebeerai.com/m/admin/?page=call&pi=restapi"


class TestLogin(unittest.TestCase):

    def test_login(self):
        domain = urlsplit(URL).netloc
        username, secret, password = netrc().authenticators(domain)
        client = PHPListClient(URL, secret=secret)
        client.login(username, password)
