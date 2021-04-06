#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) > 0:
        if len(line) >=2 and line[0] != 'Region':
	    itemType = line[2]

	    print '%s\t%s' % (itemType, 1)
