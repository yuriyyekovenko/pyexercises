from datetime import datetime
import os
from xml.etree.ElementTree import ElementTree, Element, SubElement

from ird.tests.utils.misc import wait_for


class WatchFolderHelper:

    def __init__(self, watch_folder):
        self.watch_folder = watch_folder

    def inject_program_xml_file(self, program_name, filename=None):
        if filename is None:
            filename = f'{datetime.now().timestamp()}.xml'

        root = Element("program")
        SubElement(root, "name").text = program_name
        tree = ElementTree(root)
        tree.write(os.path.join(self.watch_folder, filename))
        return filename

    def is_program_file_consumed(self, filename, timeout=60):
        return wait_for(
            lambda: not os.path.isfile(os.path.join(self.watch_folder, filename)),
            timeout
        )

