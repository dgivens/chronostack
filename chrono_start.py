#!/usr/bin/env python
import chronostack.cli
from chronostack.config import config
from chronostack.messaging import Consumer


def main():
    amqp_url = config.get('DEFAULT', 'amqp_url')
    exchange = config.get('DEFAULT', 'exchange')
    routing_key = config.get('DEFAULT', 'routing_key')

    consumer = Consumer(amqp_url, exchange, routing_key)
    try:
        consumer.run()
    except KeyboardInterrupt:
        consumer.exit()


if __name__ == '__main__':
    main()
