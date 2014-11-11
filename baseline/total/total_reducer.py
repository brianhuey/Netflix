#!/usr/bin/env python
import sys
""" Calculate the total number of users/movies in the training set"""
sum_total = 0
for line in sys.stdin:
    fields = line.strip().split(",")
    sum_total += int(fields[1])
print '%s,%s' % ('total', sum_total)
