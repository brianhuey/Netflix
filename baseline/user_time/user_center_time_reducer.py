#!/usr/bin/env python
import sys, datetime, math
""" Input: Training set with global averages appended and sqrt(movie_time)
    Calculates the time since the user last rated movie
    Output: sqrt(time last rated)"""
current_user = None
user_list = []
total = 0
count = 0
for line in sys.stdin:
    user, movie, rating, date, movie_avg, user_avg, centered_movie_time, user_time = line.strip().split("\t", 7)
    if current_user == user:
        user_list.append([movie, user, rating, date, movie_avg, user_avg, centered_movie_time, user_time])
        count += 1
    else:
        if current_user:
            for i in range(0, len(user_list)):
                total += float(user_list[i][7])
            for j in range(0, len(user_list)):
                movieid = user_list[j][0]
                rating = user_list[j][2]
                date = user_list[j][3]
                movie_avg = user_list[j][4]
                user_avg = user_list[j][5]
                centered_movie_time = user_list[j][6]
                user_time = float(user_list[j][7])
                centered_user_time = user_time - (total/count)
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movieid, current_user, rating, date, movie_avg, user_avg, centered_movie_time, centered_user_time)
        user_list = [[movie, user, rating, date, movie_avg, user_avg, centered_movie_time, user_time]]
        count = 1
        total = 0
        current_user = user
if user == current_user:
    for i in range(0, len(user_list)):
        total += float(user_list[i][7])
    for j in range(0, len(user_list)):
        movieid = user_list[j][0]
        rating = user_list[j][2]
        date = user_list[j][3]
        movie_avg = user_list[j][4]
        user_avg = user_list[j][5]
        centered_movie_time = user_list[j][6]
        user_time = float(user_list[j][7])
        centered_user_time = user_time - (total/count)
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movieid, current_user, rating, date, movie_avg, user_avg, centered_movie_time, centered_user_time)