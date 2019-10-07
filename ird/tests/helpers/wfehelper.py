import requests

from ird.tests.utils.misc import wait_for


class WorkflowEngineRestHelper:

    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session if session is not None else requests.Session()

    def get_processes(self, program_id=None, status=None):
        response = self.session.get(f'{self.base_url}/processes')
        assert response.status_code == 200
        data = response.json()

        if status:
            data = [p for p in data if p['status'] == status]
        if program_id:
            data = [p for p in data if p['program_id'] == program_id]

        return data

    def program_process_exists(self, program_id):
        data = self.get_processes(program_id=program_id)
        return len(data) > 0

    def is_program_process_completed(self, program_id, timeout=180):

        def f():
            data = self.get_processes(program_id=program_id, status='completed')
            return len(data) > 0

        return wait_for(f, timeout)
