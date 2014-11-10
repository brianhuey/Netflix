#!/usr/bin/env python
import sys
""" Create dictionary with average number of movies rated for each user,
	average number of user ratings for each movie"""

for line in sys.stdin:
    fields = line.strip().split(",")
    #print fields
    print '%s,%s,%s,%s' % (fields[0], fields[1], fields[2], fields[3])


                  
