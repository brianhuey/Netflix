#!/usr/bin/env python
import sys, random
""" Splits training_set.txt in to pre and post 2005, use
    org.apache.hadoop.mapred.lib.IdentityReducer for the
    reducer """
for line in sys.stdin:
    # populate sample list with 100k obs
    movie, user, rating, date = line.strip().split(",",3)
    date_int = int(date[0:4])
    if date_int < 2005:
        print '%s,%s,%s,%s,%s' % ('pre', movie, user, rating, date)
    # once sample is populated, generate random number
    else:
        print '%s,%s,%s,%s,%s' % ('post', movie, user, rating, date)
