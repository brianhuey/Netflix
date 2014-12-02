#!/usr/bin/env python
import sys
""" input: training set
    output: key as movieid"""
for line in sys.stdin:
    fields = line.strip().split(",")
    if len(fields) == 4:
        print '%s\t%s\t%s\t%s' % (fields[0], fields[1], fields[2], fields[3])