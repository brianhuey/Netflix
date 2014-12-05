#!/usr/bin/env python
import sys, math
""" Calculate the time coefficient basd on Koren, Bell
    for each user.
    Output: user, coefficient"""
current_user = None
theta_list = []
count = 0
total_movies = 17750 # Calculated
total_users = 480189 # Calculated
overall_rate = (100480507/float(total_movies * total_users))
for line in sys.stdin:
    user, movie, rating, date, movie_avg, user_avg, movie_time, user_time = line.strip().split("\t", 7)
    residual = overall_rate - float(movie_avg) - float(user_avg)
    # This executes if we haven't reached a different movieid
    if current_user == user:
        if float(user_time) == 0:
            theta_num = 0
            theta_den = 1
        else:
            theta_num = residual*float(user_time)
            theta_den = float(user_time)**2
        theta_list.append([theta_num, theta_den])
        count += 1
    else:
        # This executes if we reach a new movieid
        if current_user:
            total_num = 0
            total_den = 0
            for i in range(0, len(theta_list)):
                total_num += theta_list[i][0]
                total_den += theta_list[i][1]
            print '%s\t%s\t%s' % (current_user, total_num/total_den, count)
        if float(user_time) == 0:
            theta_num = 0
            theta_den = 1
        else:
            theta_num = residual*float(user_time)
            theta_den = float(user_time)**2
        # This executes only on the first line of the input
        theta_list = [[theta_num, theta_den]]
        count = 1
        current_user = user
# This executes after the last line, in the event a print didn't happen.
if user == current_user:
    total_num = 0
    total_den = 0
    for i in range(0, len(theta_list)):
        total_num += theta_list[i][0]
        total_den += theta_list[i][1]
    print '%s\t%s\t%s' % (current_user, total_num/total_den, count)