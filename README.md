# Chronostack

The eventual goal of Chronostack is to measure the timing of Heat resources
using the notifications functionality within Openstack. Currently, Heat only
generates notifications for stack actions (create, update, and delete). Since
stacks can vary greatly from one to another, the timing for stack actions is
not something that can be corrolated.

This is a starting point. Work needs to be done on the Heat side to add
notifications for individual resources. This service will need to be updated to
handle those notifications based on the format the messages take coming from
Heat.

## Enabling notifications

To enable notifications, in the Heat config, you need to add the following to
the `DEFAULT` section:

```
notification_driver=messagingv2
```

Once that is set, notifications will be set to the heat exchange. The messages
that we care about for stack actions (and hopefully resource actions), will be
sent to `notifications.info`.

## Running the service

You will need the following:

* Heat setup to emit notifications
* RabbitMQ
* statsd service (such as pystatsd)
* Graphite

First, you'll need to update the config located in `etc/chronostack.cfg`. The
settings are pretty clear as to what they do. Note that there is a `-c` flag
that allows you to specify an alternate path for the config file.

Assuming you're going the virtualenv route, you can do the following:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python chrono_start.py
```

## Credits

Created by Daniel Givens <daniel.givens@rackspace.com>
