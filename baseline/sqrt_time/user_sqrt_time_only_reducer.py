#!/usr/bin/env python
import sys, datetime, math
""" Input: Training set with global averages appended and sqrt(movie_time)
    Output: the date the user first rated a movie"""
current_user = None
user_list = []
for line in sys.stdin:
    user, movie, rating, date, movie_avg, user_avg, movie_time = line.strip().split("\t", 6)
    if current_user == user:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user_list.append([movie, rating, date, movie_avg, user_avg, movie_time])
    else:
        if current_user:
            datelist = sorted(user_list, key=lambda x: x[2])
            print '%s\t%s' % (current_user, datelist[0][2])
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user_list = [[movie, rating, date, movie_avg, user_avg, movie_time]]
        current_user = user
if user == current_user:
    datelist = sorted(user_list, key=lambda x: x[2])
    print '%s\t%s' % (current_user, datelist[0][2])