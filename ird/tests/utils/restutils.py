import requests


class RestHelper:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self):
        return requests.get(self.endpoint)