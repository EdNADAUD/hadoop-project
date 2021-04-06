#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) > 0:
        if len(line) >=13 and line[0] != 'Region':
	    country = line[1]
	    totalProfit = line[13][:-1]

	    print '%s\t%s' % (country, totalProfit)
