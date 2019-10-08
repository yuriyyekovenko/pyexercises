import random
from string import ascii_lowercase
from time import sleep


def generate_unique_program_name(wfe, mm):
    program = None
    unique = False
    while not unique:
        program = ''.join(random.choice(ascii_lowercase) for _ in range(10))
        unique = not (wfe.program_process_exists(program) or
                      mm.program_exists(program))
    return program


def wait_for(func, timeout, step=1):
    attempts = timeout / step
    while attempts:
        if func():
            return True
        sleep(step)
        attempts -= 1
    return False
