#!/usr/bin/env python
import sys, math
""" Create dictionary with movie as a key, sort by date and
    calculate the time since the movie was last rated"""
current_user = None
theta_list = []
count = 0
total_movies = 17750 # Calculated
total_users = 480189 # Calculated
overall_rate = (100480507/float(total_movies * total_users))
for line in sys.stdin:
    user, movie, rating, date, movie_avg, user_avg, movie_time, user_time = line.strip().split("\t", 7)
    residual = overall_rate - float(movie_avg) - float(user_avg)
    if current_user == user:
        if float(user_time) == 0:
            theta = 0
        else:
            theta = (residual*float(user_time))/float(user_time)**2
        theta_list.append(theta)
        count += 1
    else:
        if current_user:
            total = 0
            for i in range(0, len(theta_list)):
                total += theta_list[i]
            print '%s\t%s\t%s' % (current_user, total, count)
        if float(movie_time) == 0:
            theta = 0
        else:
            theta = (residual*float(movie_time))/float(movie_time)**2
        theta_list = [theta]
        count = 1
        current_user = user
if user == current_user:
    total = 0
    for i in range(0, len(theta_list)):
        total += theta_list[i]
    print '%s\t%s\t%s' % (current_user, total, count)