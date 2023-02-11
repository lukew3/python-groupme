import requests

class GroupMe:
    def __init__(self, token):
        self.token = token

    def groups(self):
        params = { 'token': self.token }
        return requests.get('https://api.groupme.com/v3/groups', params=params).json()

