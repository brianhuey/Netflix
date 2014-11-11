#!/usr/bin/env python
import sys, math
""" Process user totals to calculate rating rate per movie
    """
total_movies = 17750 # Calculated
dictionary = {}
for line in sys.stdin:
    key, value = line.strip().split(",", 1)
    dictionary[key] = value

def calc_avg(dictionary):
    sum_total = 0
    avg = 0
    for key in dictionary:
        sum_total += int(dictionary[key])
        #print fields
    avg = round(sum_total/float(total_movies),2)
    return avg

def stdev(dictionary):
    deviation = 0
    avg = calc_avg(dictionary)
    for line in dictionary:
        deviation += math.pow(int(dictionary[key])-avg,2)
    stdev = round(math.sqrt(deviation/float(total_movies)),6)
    return stdev

print calc_avg(dictionary)
print stdev(dictionary)

