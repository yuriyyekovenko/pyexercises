import requests


class MediaManagerRestHelper:

    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session if session is not None else requests.Session()

    def program_exists(self, program_name):
        response = self.session.get(f'{self.base_url}/entities/program/{program_name}')
        return response.status_code == 200
