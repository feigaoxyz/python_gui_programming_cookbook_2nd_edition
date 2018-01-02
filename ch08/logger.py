import os

import time
from datetime import datetime


class LogLevel:
    OFF = 0
    MINIMUM = 1
    NORMAL = 2
    DEBUG = 3


class Logger:
    def __init__(self, full_test_name, loglevel=LogLevel.DEBUG):
        test_name = os.path.splitext(os.path.basename(full_test_name))[0]
        log_name = test_name + '.log'

        logs_folder = 'logs'
        if not os.path.exists(logs_folder):
            os.makedirs(logs_folder, exist_ok=True)

        self.log = os.path.join(logs_folder, log_name)
        self.create_log()

        self.logging_level = loglevel
        self.start_time = time.perf_counter()

    def create_log(self):
        with open(self.log, mode='w') as log_file:
            log_file.write(self.get_datetime() + '\t\t*** Starting Test ***\n')

    def get_datetime(self):
        return str(datetime.now())

    def write_to_log(self, msg='', loglevel=LogLevel.DEBUG):
        if loglevel > self.logging_level:
            return
        with open(self.log, mode='a') as log_file:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
            log_file.write(self.get_datetime() + '\t\t' + msg + '\n')
