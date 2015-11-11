# Centrally handle the cli args

import argparse

parser = argparse.ArgumentParser(description='Process ')
parser.add_argument('-c', '--config', help='Path to config file',
                    default='etc/chronostack.cfg')
args = parser.parse_args()
