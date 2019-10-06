import requests

from ird import configuration


class WFEProcess:

    def __init__(self, name, program_id, status):
        self.name = name
        self.program_id = program_id
        self.status = status


class WFERestHelper:

    def __init__(self):
        self.base_url = configuration.WFE_BASE_URL

    def get_processes(self, status=None, program_id=None):
        response = requests.get(f'{self.base_url}/processes')
        assert response.status_code == 200
        data = response.json()

        if status:
            data = [p for p in data if p['status'] == status]
        if program_id:
            data = [p for p in data if p['program_id'] == program_id]

        return data

    def get_fake(self):
        response = requests.get('http://jsonplaceholder.typicode.com/todos', timeout=180)
        assert response.status_code == 200
        return response


if __name__ == '__main__':
    p = WFEProcess(**{'name': '123234', 'program_id': 'pro1', 'status': 'running'})
    print(p.status)
