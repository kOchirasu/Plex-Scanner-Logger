import os
import sys
import inspect
import traceback
import logging
from logging.handlers import RotatingFileHandler

# Set Plex root directory 2 levels above Scanners/SCANNER_TYPE
PLEX_ROOT = os.path.abspath(os.path.join(os.path.dirname(
    inspect.getfile(inspect.currentframe())), "..", ".."))
PLEX_LOGS = os.path.join(PLEX_ROOT, 'Logs')

# Logger class imitates LogKit from Plex Plug-in Framework to be used with scanners
class Logger():

    def __init__(self, filename, logLevel=logging.DEBUG):
        handler = RotatingFileHandler(
            os.path.join(PLEX_LOGS, filename + '.log'),
            mode='w',
            maxBytes=1024 * 1024, # 1MB
            backupCount=5
        )
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(filename)
        self.logger.addHandler(handler)
        self.logger.setLevel(logLevel)

    def Debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def Info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def Warn(self, msg, *args, **kwargs):
        self.logger.warn(msg, *args, **kwargs)

    def Error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def Critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def Exception(self, msg, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)

    def Stack(self):
        stack = ''
        lines = traceback.format_stack()[3:-3]
        for line in lines:
            if sys.prefix not in line:
                stack += '  %s\n' % line.strip()
        self.Debug("Current stack:\n" + stack)

    def __call__(self, msg, *args, **kwargs):
        self.Info(msg, *args, **kwargs)
