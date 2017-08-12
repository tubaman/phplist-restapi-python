import requests


class PHPListClient:

    def __init__(self, url, secret=None):
        self.url = url
        self.secret = secret
        self.session = requests.Session()

    def call_api(self, command, params):
        params['cmd'] = command
        if self.secret:
            params['secret'] = self.secret
        r = self.session.post(self.url, data=params)
        r.raise_for_status()
        output = r.json()
        assert output['status'] == 'success'
        return output

    def login(self, username, password):
        params = {
            'login': username,
            'password': password,
        }
        self.call_api('login', params)
