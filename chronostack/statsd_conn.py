import statsd
from chronostack.config import config


host = config.get('statsd', 'host')
port = config.get('statsd', 'port')
region = config.get('statsd', 'region')
statsd_conn = statsd.StatsClient(host, port, prefix=region)
