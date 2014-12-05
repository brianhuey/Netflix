#!/usr/bin/env python
import sys, datetime, math
""" Input: Training set with global averages appended
    Calculates the time since the movie was last rated
    Output: sqrt(time last rated)"""
current_movie = None
for line in sys.stdin:
    movie, count = line.strip().split("\t", 1)
    if current_movie == movie:
        # Convert to date object
        continue
    else:
        if current_movie:
            print '%s' % (movie)
        current_movie = movie
# On last line, emit the contents of the final list
if movie == current_movie:
    print '%s' % (movie)