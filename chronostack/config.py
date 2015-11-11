# Centrally handle the config object

import ConfigParser
import sys
from chronostack.cli import args

config_file = args.config

config = ConfigParser.ConfigParser()
try:
    config.read(config_file)
except IOError:
    print('Config file {} does not exist'.format(config_file))
    sys.exit(1)
