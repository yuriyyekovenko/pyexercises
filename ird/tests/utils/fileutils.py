from datetime import datetime
import os
from time import sleep
from xml.etree.ElementTree import ElementTree, Element, SubElement

from ird.configuration import QTS_WATCH_FOLDER


def inject_program_xml_file(program_name, filename=None):
    if filename is None:
        filename = f'{datetime.now().timestamp()}.xml'

    root = Element("program")
    SubElement(root, "name").text = program_name
    tree = ElementTree(root)
    tree.write(os.path.join(QTS_WATCH_FOLDER, filename))
    return filename


def check_program_file_consumed(filename, timeout=60):
    return wait_for(lambda: os.path.isfile(os.path.join(QTS_WATCH_FOLDER, filename)),
                    timeout)


def wait_for(func, timeout, step=1):
    attempts = timeout / step
    while attempts:
        if func():
            return True
        sleep(step)
        attempts -= 1
    return False
