from unittest.mock import Mock
import os
import re

from irdeto.configuration import PROTOCOL
from irdeto.tests.utils.misc import generate_unique_program_name

"""
The module verifies positive scenario of a program publishing.

It also contains temporary code mocking external calls including
os.path.isfile method. 
It allows running of the test-case to ensure it's really executable.

To enable mocking, adjust PROTOCOL value in configuration.py module.   
"""

if PROTOCOL == 'mock':
    os.path.isfile = Mock()
    os.path.isfile.return_value = False

    mocked_processes = [
        {
            "name": "process1",
            "program_id": "process1",
            "status": "completed"
        },
        {
            "name": "process2",
            "program_id": "program2",
            "status": "running"
        }
    ]


def test_program_publishing(wfe, mm, folder):
    if PROTOCOL == 'mock':
        adapter = wfe.session.get_adapter('mock')
        adapter.register_uri('GET', '//wfe/processes', json=mocked_processes)
        adapter.register_uri('GET', re.compile('//mm/entities/program'), status_code=404)

    program = generate_unique_program_name(wfe, mm)

    if PROTOCOL == 'mock':
        mocked_processes.append({
            "name": "process3",
            "program_id": program,
            "status": "completed"
        })
        adapter.register_uri('GET', '//wfe/processes', json=mocked_processes)
        adapter.register_uri('GET', f'//mm/entities/program/{program}', status_code=200)

    filename = folder.inject_program_xml_file(program)
    assert folder.is_program_file_consumed(filename, timeout=60), \
        'File should be consumed within 60 seconds'

    assert wfe.program_process_exists(program), \
        'The process for just consumed file should be created in the Workflow Engine'
    assert wfe.is_program_process_completed(program, timeout=180), \
        'The `consumer` process should complete within 180 seconds'
    assert mm.program_exists(program), \
        'The result of the process should be published to Media Manager'
