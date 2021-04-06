#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) > 0:
        if len(line) >=3 and line[0] != 'Region':
	        salesChannel = line[3]

	    print '%s\t%s' % (salesChannel, 1)
