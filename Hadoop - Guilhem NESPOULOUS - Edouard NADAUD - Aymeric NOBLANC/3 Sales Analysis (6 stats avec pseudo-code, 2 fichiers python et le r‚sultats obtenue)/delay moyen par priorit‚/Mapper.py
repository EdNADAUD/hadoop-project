#!/usr/bin/python

import sys
from datetime import date

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) > 0:
        if len(line) >=7 and line[0] != 'Region':
	    priority = line[4]
	    delay = (date(int(line[7].split("/")[2]),int(line[7].split("/")[0]),int(line[7].split("/")[1]))-date(int(line[5].split("/")[2]),int(line[5].split("/")[0]),int(line[5].split("/")[1]))).days

	    print '%s\t%s' % (priority, delay)
