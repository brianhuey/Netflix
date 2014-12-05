#!/usr/bin/env python
import sys
""" Input: movie, user, rating, date, movie_avg, user_avg,
           centered_movie_time
    Output: Same data with user as key"""
for line in sys.stdin:
    fields = line.strip().split("\t")
    #print fields
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (fields[1], fields[0], fields[2], fields[3], fields[4], fields[5], fields[6])
