#!/usr/bin/env python
import sys
""" Input: Training data with user and movie avgs joined
    Output: Same data with movie as key"""

for line in sys.stdin:
    fields = line.strip().split("\t")
    #print fields
    print '%s\t%s\t%s\t%s\t%s\t%s' % (fields[0], fields[1], fields[2], fields[3], fields[4], fields[5])
