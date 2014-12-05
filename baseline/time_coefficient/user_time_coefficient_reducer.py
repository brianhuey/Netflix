#!/usr/bin/env python
import sys, math
""" Create dictionary with movie as a key, sort by date and
    calculate the time since the movie was last rated"""
current_user = None
theta_list = []
user_list = []
count = 0
for line in sys.stdin:
    user, movie, rating, date, movie_avg, user_avg, movie_time, user_time, movie_coeff, movie_n = line.strip().split("\t", 9)
    residual = 1 - float(movie_avg) - float(user_avg)
    if current_user == user:
        if float(user_time) == 0:
            theta = 0
        else:
            theta = (residual*float(user_time))/float(user_time)**2
        theta_list.append(theta)
        user_list.append([movie,user,rating,date,movie_avg,user_avg,movie_time,user_time,movie_coeff,movie_n])
        count += 1
    else:
        if current_user:
            total = 0
            for i in range(0, len(theta_list)):
                total += theta_list[i]
            for i in range(0, len(user_list)):
                movie = user_list[i][0]
                user = user_list[i][1]
                rating= user_list[i][2]
                date = user_list[i][3]
                movie_avg = user_list[i][4]
                user_avg = user_list[i][5]
                movie_time = user_list[i][6]
                user_time = user_list[i][7]
                movie_coeff = user_list[i][8]
                movie_n = user_list[i][9]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movie, user, rating, date, movie_avg,
                    user_avg, movie_time, user_time, movie_coeff, movie_n, total, count)
        theta_list = []
        user_list = []
        count = 0
        current_user = user