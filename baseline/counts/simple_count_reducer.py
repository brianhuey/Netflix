#!/usr/bin/env python
import sys
""" Create dictionary with average number of movies rated for each user,
    average number of user ratings for each movie"""
count = 0
for line in sys.stdin:
    data = line.strip().split('\t')
    count += int(data[1])
print count

