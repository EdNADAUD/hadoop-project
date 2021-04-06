#!/usr/bin/python

#Reducer.py
import sys

region_unitSold = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    region, unitSold = line.split('\t')

    if region in region_unitSold:
        region_unitSold[region].append(int(unitSold))
    else:
        region_unitSold[region] = []
        region_unitSold[region].append(int(unitSold))

#Reducer
for region in region_unitSold.keys():
    ave_unitSold = sum(region_unitSold[region])*1.0 / len(region_unitSold[region])
    print '%s\t%s'% (region, ave_unitSold)
