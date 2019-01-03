import logging
import sys

LEVELS = {'debug':logging.DEBUG,
          'info':logging.INFO,
          'warning':logging.WARNING,
          'error':logging.ERROR,
          'critical':logging.CRITICAL,}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug("this is a debug message")
logging.info("this is an info message")
logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical error message")