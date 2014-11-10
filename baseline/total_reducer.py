#!/usr/bin/env python
import sys
""" Create dictionary with average number of movies rated for each user,
	average number of user ratings for each movie"""
sum_total = 0
for line in sys.stdin:
    fields = line.strip().split(",")
    sum_total += fields[1]
    print '%s,%s' % ('total', sum_total)
