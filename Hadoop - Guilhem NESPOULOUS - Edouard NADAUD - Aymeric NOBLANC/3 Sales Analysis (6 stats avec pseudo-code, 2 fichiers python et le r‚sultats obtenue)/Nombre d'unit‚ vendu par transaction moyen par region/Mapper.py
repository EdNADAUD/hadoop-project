#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) > 0:
        if len(line) >=8 and line[0] != 'Region':
	    region = line[0]
	    unitSold = line[8]

	    print '%s\t%s' % (region, unitSold)
