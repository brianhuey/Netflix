#!/usr/bin/env python
import sys, math
""" Calculates the user_id-specific global effect
    Input: user_total_fromAWS
    Output: user_id, #ratings/moviess - overall average rating
    """
total_movies = 17750 # Calculated
total_users = 480189 # Calculated
overall_rate = (100480507/float(total_movies * total_users))
dictionary = {}
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    if key == 'total users':
        continue
    else:
        dictionary[key] = value
total = 0
deviation = 0
for line in dictionary:
    deviation = int(dictionary[line]) / float(total_movies)
    dictionary[line] = deviation - overall_rate
    total += dictionary[line]
    print '%s\t%s' % (line, dictionary[line])
# print total # Used for checking the sum of deviations: should be ~0