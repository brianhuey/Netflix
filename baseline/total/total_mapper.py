#!/usr/bin/env python
import sys
""" Map the results of movie_total_reducer or user_total_reducer"""

for line in sys.stdin:
    fields = line.strip().split(",")
    #print fields
    if fields[0][0:5] == 'total':
        print '%s,%s' % ('total', fields[1])
