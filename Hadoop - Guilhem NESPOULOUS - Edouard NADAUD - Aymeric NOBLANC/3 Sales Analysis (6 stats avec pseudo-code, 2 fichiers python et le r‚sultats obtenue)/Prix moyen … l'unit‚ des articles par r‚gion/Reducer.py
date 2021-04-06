#!/usr/bin/python
#Reducer.py
import sys

region_unitPrice = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    region, unitPrice = line.split('\t')

    if region in region_unitPrice:
        region_unitPrice[region].append(float(unitPrice))
    else:
        region_unitPrice[region] = []
        region_unitPrice[region].append(float(unitPrice))

#Reducer
for region in region_unitPrice.keys():
    ave_unitPrice = sum([float(i) for i in region_unitPrice[region]])*1.0 / len(region_unitPrice[region])
    print '%s\t%s'% (region, ave_unitPrice)
