import logging
from chronostack.config import config


config_log_level = config.get('logging', 'level')
if config_log_level == 'DEBUG':
    log_level = logging.DEBUG
if config_log_level == 'INFO':
    log_level = logging.INFO
if config_log_level == 'WARNING':
    log_level = logging.WARNING
if config_log_level == 'ERROR':
    log_level = logging.ERROR
if config_log_level == 'CRITICAL':
    log_level = logging.CRITICAL

logger = logging.getLogger(__name__)
logger.setLevel(log_level)

formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')

stdout = config.get('logging', 'stdout')

ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(formatter)
logger.addHandler(ch)

log_file = config.get('logging', 'log_file')

fh = logging.FileHandler(log_file)
fh.setLevel(log_level)
fh.setFormatter(formatter)
logger.addHandler(fh)
