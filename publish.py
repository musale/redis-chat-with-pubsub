"""Publishing into the channel."""

import sys

from settings import r

if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]

    print ('Welcome to {channel}'.format(**locals()))

    while True:
        # freeze the DOS pop-up
        message = input('Enter a message: ')

        if message.lower() == 'exit':
            break

        message = '{name} says: {message}'.format(**locals())

        r.publish(channel, message)
