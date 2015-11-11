import redis
from chronostack.config import config

redis_host = config.get('redis', 'host')
redis_port = config.get('redis', 'port')
redis_db = config.get('redis', 'db')

redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
