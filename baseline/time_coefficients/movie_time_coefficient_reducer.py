#!/usr/bin/env python
import sys, math
""" Create dictionary with movie as a key, sort by date and
    calculate the time since the movie was last rated"""
current_movie = None
theta_list = []
movie_list = []
count = 0
for line in sys.stdin:
    movie, user, rating, date, movie_avg, user_avg, movie_time, user_time = line.strip().split("\t", 7)
    residual = 1 - float(movie_avg) - float(user_avg)
    if current_movie == movie:
        if float(movie_time) == 0:
            theta = 0
        else:
            theta = (residual*float(movie_time))/float(movie_time)**2
        theta_list.append(theta)
        movie_list.append([movie,user,rating,date,movie_avg,user_avg,movie_time,user_time])
        count += 1
    else:
        if current_movie:
            total = 0
            for i in range(0, len(theta_list)):
                total += theta_list[i]
            for i in range(0, len(movie_list)):
                movie = movie_list[i][0]
                user = movie_list[i][1]
                rating= movie_list[i][2]
                date = movie_list[i][3]
                movie_avg = movie_list[i][4]
                user_avg = movie_list[i][5]
                movie_time = movie_list[i][6]
                user_time = movie_list[i][7]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movie, user, rating, date, movie_avg,
                    user_avg, movie_time, user_time, total, count)
        theta_list = []
        movie_list = []
        count = 0
        current_movie = movie