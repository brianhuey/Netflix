#!/usr/bin/env python
import sys, math
""" Process user totals to calculate rating rate per movie
    """
total_movies = 17750 # Calculated
total_users = 431198 # Calculated
total_obs = 0
for line in sys.stdin:
    key, value = line.strip().split(",", 1)
    total_obs += int(value)
print total_obs


