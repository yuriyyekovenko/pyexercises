# from unittest.mock import Mock, patch
import requests

from ird.tests.basetest import BaseTest
from ird.tests.utils.fileutils import inject_program_xml_file, check_program_file_consumed, wait_for
from ird.tests.utils.wfehelper import WFERestHelper
import requests_mock


class TestProgramPublishing(BaseTest):
    """
    Start with creating a file and putting it to the folder.
    Verify the process is running.
    When process is completed verify that data is created in Media Manager.

    - add new xml file
    - wait for file to be consumed (within 60s).
      - fail if not consumed within 60 seconds
    - once the file disappears check if the process appears in wfe in Running state
    - wait for 180 seconds - process should go to Completed
      - fail if process disappears or does not go to Completed within timeout
    - check if program appeared in media manager
    """

    def test_program_publishing(self):
        program = 'program1'

        filename = inject_program_xml_file(program)
        check_program_file_consumed(filename, timeout=60)

        # check_program_process_is_running(program)
        assert len(self.wfe.get_processes(program, 'running')) == 1

        # check_program_process_completed(program, timeout=180)
        wait_for(len(self.wfe.get_processes(program, 'completed')) == 1, 180)

        # check_program_added_to_media_manager(program)

        response = self.wfe.get_fake()
        print(response.json())

    # @requests_mock.Mocker()
    def test_2(self):
        with requests_mock.Mocker() as m:
            m.get('http://jsonplaceholder.typicode.com/todos', text='resp2')
            assert requests.get('http://jsonplaceholder.typicode.com/todos').text == 'resp'