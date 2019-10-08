import pytest

import requests
import requests_mock

from irdeto.configuration import WFE_BASE_URL, MM_BASE_URL, QTS_WATCH_FOLDER
from irdeto.tests.helpers.mmhelper import MediaManagerRestHelper
from irdeto.tests.helpers.wfehelper import WorkflowEngineRestHelper
from irdeto.tests.helpers.folderhelper import WatchFolderHelper


# configuring requests mock
session = requests.Session()
adapter = requests_mock.Adapter()
session.mount('mock', adapter)


@pytest.fixture(scope='module')
def wfe():
    return WorkflowEngineRestHelper(WFE_BASE_URL, session)


@pytest.fixture(scope='module')
def mm():
    return MediaManagerRestHelper(MM_BASE_URL, session)


@pytest.fixture(scope='module')
def folder():
    return WatchFolderHelper(QTS_WATCH_FOLDER)
