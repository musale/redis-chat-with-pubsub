"""Subscribe to a given channel and get the messages."""

import sys

from settings import r

if __name__ == '__main__':
    channel = sys.argv[1]

    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print ('Listening to {channel}'.format(**locals()))

    while True:
        for item in pubsub.listen():
            print (item['data'])
