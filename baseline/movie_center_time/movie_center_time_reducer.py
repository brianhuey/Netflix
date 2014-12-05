#!/usr/bin/env python
import sys, math
""" Calculates the average and centers the movie sqrt(time) value around the mean
    Output: Data input with centered sqrt(time last rated)"""
current_movie = None
movie_list = []
total = 0
count = 0
for line in sys.stdin:
    movie, user, rating, date, movie_avg, user_avg, movie_time = line.strip().split("\t", 6)
    if current_movie == movie:
        movie_list.append([movie, user, rating, date, movie_avg, user_avg, movie_time])
        count += 1
    else:
        if current_movie:
            for i in range(0, len(movie_list)):
                total += float(movie_list[i][6])
            for j in range(0, len(movie_list)):
                userid = movie_list[j][1]
                rating = movie_list[j][2]
                date = movie_list[j][3]
                movie_avg = movie_list[j][4]
                user_avg = movie_list[j][5]
                movie_time = float(movie_list[j][6])
                centered_movie_time = movie_time - (total/count)
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_movie, userid, rating,
                    date, movie_avg, user_avg, centered_movie_time)
        movie_list = [[movie, user, rating, date, movie_avg, user_avg, movie_time]]
        count = 1
        total = 0
        current_movie = movie
# On last line, emit the contents of the final list
if movie == current_movie:
    for i in range(0, len(movie_list)):
        total += float(movie_list[i][6])
    for j in range(0, len(movie_list)):
        userid = movie_list[j][1]
        rating = movie_list[j][2]
        date = movie_list[j][3]
        movie_avg = movie_list[j][4]
        user_avg = movie_list[j][5]
        movie_time = float(movie_list[j][6])
        centered_movie_time = movie_time - (total/count)
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_movie, userid, rating, date,
            movie_avg, user_avg, centered_movie_time)
