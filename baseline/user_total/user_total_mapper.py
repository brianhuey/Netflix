#!/usr/bin/env python
import sys
""" Input: movie, user, rating, date
    Output: Same data with user as key"""
for line in sys.stdin:
    fields = line.strip().split(",")
    #print fields
    print '%s\t%s\t%s\t%s' % (fields[1], fields[0], fields[2], fields[3])
