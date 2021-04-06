#!/usr/bin/python

#Reducer.py
import sys

nbSalesChannel= {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    salesChannel, arr = line.split('\t')

    if salesChannel in nbSalesChannel:
        nbSalesChannel[salesChannel] += 1
    else:
        nbSalesChannel[salesChannel] = 1

#Reducer
for salesChannel in nbSalesChannel.keys():
    print '%s\t%s'% (salesChannel, nbSalesChannel[salesChannel])
