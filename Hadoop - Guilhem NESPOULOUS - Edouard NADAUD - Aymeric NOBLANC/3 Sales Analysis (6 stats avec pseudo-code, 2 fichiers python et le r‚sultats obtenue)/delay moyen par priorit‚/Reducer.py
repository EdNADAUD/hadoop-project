#!/usr/bin/python

#Reducer.py
import sys

priority_delay = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    priority, delay = line.split('\t')

    if priority in priority_delay:
        priority_delay[priority].append(int(delay))
    else:
        priority_delay[priority] = []
        priority_delay[priority].append(int(delay))

#Reducer
for priority in priority_delay.keys():
    ave_delay = sum(priority_delay[priority])*1.0 / len(priority_delay[priority])
    print '%s\t%s'% (priority, ave_delay)
