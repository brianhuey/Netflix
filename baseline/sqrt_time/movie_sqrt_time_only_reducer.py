#!/usr/bin/env python
import sys, datetime, math
""" Input: Training set with global averages appended, movie as key
    Output: movie, date movie first rated"""
current_movie = None
movie_list = []
for line in sys.stdin:
    movie, user, rating, date, movie_avg, user_avg = line.strip().split("\t", 5)
    if current_movie == movie:
        # Convert to date object
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        movie_list.append([user,rating, date, movie_avg, user_avg])
    else:
        if current_movie:
            datelist = sorted(movie_list, key=lambda x: x[2])
            print '%s\t%s' % (current_movie, datelist[0][2])
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        movie_list = [[user,rating,date,movie_avg,user_avg]]
        current_movie = movie
# On last line, emit the contents of the final list
if movie == current_movie:
    datelist = sorted(movie_list, key=lambda x: x[2])
    print '%s\t%s' % (current_movie, datelist[0][2])
