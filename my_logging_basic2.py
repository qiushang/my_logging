import glob
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
import time

LOG_FILENAME = "logging_rotatingfile_example.out"

# set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# add the log message handler to the logger
handler = TimedRotatingFileHandler("time_rotating_test", "s", 3)
# 设置后缀名称，跟strftime的格式一样
handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
# handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
#                                                maxBytes=20,
#                                                backupCount=5,)
my_logger.addHandler(handler)

# log some messages
for i in range(20):
    my_logger.debug("i = %d" % i)
    time.sleep(1)

# see what files are created
logfiles = glob.glob("%s*" % LOG_FILENAME)
for filename in logfiles:
    print(filename)