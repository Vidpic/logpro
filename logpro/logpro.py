import logging
import colorlog

class Log:
    def __init__(self, name: str):
        level = logging.DEBUG
        self.log = logging.getLogger(name)
        self.log.setLevel(level)

        handler = logging.StreamHandler()
        handler.setLevel(level)

        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s | %(levelname)s | %(message)s",
            datefmt='%H:%M:%S',
            log_colors={
                '  DEBUG   ': 'cyan',
                '   INFO   ': 'green',
                ' WARNING  ': 'yellow',
                '  ERROR   ': 'red',
                ' CRITICAL ': 'bold_red',
            }
        )

        handler.setFormatter(formatter)

        self.log.addHandler(handler)

        self.center_log_levels()

    def center_log_levels(self):
        logging.addLevelName(logging.DEBUG, "  DEBUG   ")
        logging.addLevelName(logging.INFO, "   INFO   ")
        logging.addLevelName(logging.WARNING, " WARNING  ")
        logging.addLevelName(logging.ERROR, "  ERROR   ")
        logging.addLevelName(logging.CRITICAL, " CRITICAL ")

    def get_log(self):
        return self.log
    
    def level(self, level: int):
        self.log.setLevel(level)

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

log = Log(__name__).get_log()
