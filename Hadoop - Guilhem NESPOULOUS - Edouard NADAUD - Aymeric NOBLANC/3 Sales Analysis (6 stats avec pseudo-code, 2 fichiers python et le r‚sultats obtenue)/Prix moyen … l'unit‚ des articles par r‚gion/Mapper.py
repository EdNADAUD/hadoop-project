#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) > 0:
	    if len(line) >= 9 and line[0] != 'Region':
            region = line[0]
            unitPrice = line[9]

            print '%s\t%s' % (region, unitPrice)
