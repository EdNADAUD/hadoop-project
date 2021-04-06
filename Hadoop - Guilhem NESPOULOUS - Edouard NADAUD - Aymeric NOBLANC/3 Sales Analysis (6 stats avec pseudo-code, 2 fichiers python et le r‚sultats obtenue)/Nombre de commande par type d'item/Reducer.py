#!/usr/bin/python

#Reducer.py
import sys

nbItemType= {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    itemType, arr = line.split('\t')

    if itemType in nbItemType:
        nbItemType[itemType] += 1
    else:
        nbItemType[itemType] = 1

#Reducer
for itemType in nbItemType.keys():
    print '%s\t%s'% (itemType, nbItemType[itemType])
