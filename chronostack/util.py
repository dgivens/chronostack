import re
from datetime import datetime
from chronostack.logger import logger
from chronostack.redis_conn import redis_conn as redis
from chronostack.statsd_conn import statsd_conn as statsd


def handle_message(message):
    # This is setup to handle stack notifications. Changes will be needed to
    # accomodate resources once it has been decided how Heat generates those
    # notifications.

    event_type = message.get('event_type')
    payload = message.get('payload')
    stack_id = payload.get('stack_identity')
    timestamp = message.get('timestamp')

    # If the notification is a start, then save its timestamp to redis
    if re.search('start$', event_type):
        logger.debug('Saving %s for %s to %s' % (event_type, stack_id,
                     timestamp))
        redis.set(stack_id, timestamp)

    # if the notification is an end, retreive the start timestamp from redis,
    # determine the time taken from start to end, and send a timing event to
    # statsd.
    if re.search('end$', event_type):
        event_type = re.sub('\.end$', '', event_type)
        start = redis.get(stack_id)
        logger.debug('Retrieved %s for %s from redis' % (start, stack_id))
        if start:
            start_time = datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
            end_time = datetime.strptime(message.get('timestamp'),
                                         '%Y-%m-%d %H:%M:%S.%f')
            duration_td = end_time - start_time
            duration = duration_td.total_seconds()

            logger.debug('Sending %s to statsd: %s' % (event_type, duration))
            statsd.timing(event_type, duration)

            logger.debug('Deleting key %s from redis' % stack_id)
            redis.delete(stack_id)
