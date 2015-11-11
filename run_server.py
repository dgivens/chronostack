#!/usr/bin/env python
import metrics.cli
from metrics.config import config
from metrics.messaging import Consumer


def main():
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
