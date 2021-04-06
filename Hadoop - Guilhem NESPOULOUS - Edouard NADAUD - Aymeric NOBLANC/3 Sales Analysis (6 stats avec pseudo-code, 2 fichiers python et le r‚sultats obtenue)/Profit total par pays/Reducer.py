#!/usr/bin/python

#Reducer.py
import sys

country_totalProfit = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    country, totalProfit = line.split('\t')

    if country in country_totalProfit:
        country_totalProfit[country].append(float(totalProfit))
    else:
        country_totalProfit[country] = []
        country_totalProfit[country].append(float(totalProfit))

#Reducer
for country in country_totalProfit.keys():
    totalProfit_country = sum([float(i) for i in country_totalProfit[country]])
    print '%s\t%s'% (country, totalProfit_country)
