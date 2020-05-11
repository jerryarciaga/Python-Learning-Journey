#!/usr/bin/python

import webbrowser
import sys

address = ' '.join(sys.argv[1:])

if len(sys.argv) != 1:
    webbrowser.open('https://google.com/maps/place/' + address)
else:
    print('Please type in an address.')
