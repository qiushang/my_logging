import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
import time

# debug level logger
my_logger_debug = logging.getLogger("debug_logger")
my_logger_debug.setLevel(logging.DEBUG)
"""
formatter的参数设置
"""
formatter = logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d %(message)s')   # 每行日志的前缀设置
"""
when 是一个字符串的定义如下：
“S”: Seconds
“M”: Minutes
“H”: Hours
“D”: Days
“W”: Week day (0=Monday)
“midnight”: Roll over at midnight
"""
debug_handler = TimedRotatingFileHandler("logging_debug", "midnight", 1)
debug_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
debug_handler.setFormatter(formatter)
my_logger_debug.addHandler(debug_handler)

# info level logger
my_logger_info = logging.getLogger("info_logger")
my_logger_info.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d %(message)s')   # 每行日志的前缀设置
info_handler = TimedRotatingFileHandler("logging_info", "s", 3)
info_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
info_handler.setFormatter(formatter)
my_logger_info.addHandler(info_handler)

# log some messages
for i in range(20):
    """
    my_logger_info.debug("this is a debug message 1")
    my_logger_info.info("this is an info message 1")
    my_logger_info.warning("this is a warning message 1")
    my_logger_info.error("this is an error message 1")
    my_logger_info.critical("this is a critical error message 1")
    """
    time.sleep(1)
    my_logger_debug.debug("this is a debug message")
    my_logger_debug.info("this is an info message")
    my_logger_debug.warning("this is a warning message")
    my_logger_debug.error("this is an error message")
    my_logger_debug.critical("this is a critical error message")
