#!/usr/bin/env python

import ConfigParser
import argparse
import signal
from metrics.messaging import Consumer


def main():
    parser = argparse.ArgumentParser(description='Process ')
    parser.add_argument('-c', '--config', help='Path to config file',
                        default='etc/metrics.cfg')
    args = parser.parse_args()
    config_file = args.config

    config = ConfigParser.ConfigParser()
    try:
        config.read(config_file)
    except IOError:
        print('Config file {} does not exist'.format(config_file))
        sys.exit(1)

    amqp_url = config.get('DEFAULT', 'amqp_url')
    exchange = config.get('DEFAULT', 'exchange')
    routing_key = config.get('DEFAULT', 'routing_key')

    consumer = Consumer(amqp_url, exchange, routing_key)
    try:
        consumer.run()
    except KeyboardInterrupt:
        consumer.stop()


if __name__ == '__main__':
    main()
