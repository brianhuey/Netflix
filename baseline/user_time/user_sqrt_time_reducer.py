#!/usr/bin/env python
import sys, datetime, math
""" Input: Training set with global averages appended and sqrt(movie_time)
    Calculates the time since the user last rated movie
    Output: sqrt(time last rated)"""
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
            for i in range(0, len(datelist)):
                movieid = datelist[i][0]
                rating = datelist[i][1]
                movie_avg = datelist[i][3]
                user_avg = datelist[i][4]
                movie_time = datelist[i][5]
                # reformat date back to original YYYY-MM-DD
                date = datelist[i][2].isoformat()[0:10]
                if i == 0:
                    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movieid, current_user, rating, date, movie_avg, user_avg, movie_time, 0)
                else:
                    # calculate the timedelta, use .days attribute to get days
                    timesince = (datelist[i][2] - datelist[i-1][2])
                    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movieid, current_user, rating, date, movie_avg, user_avg, movie_time, math.sqrt(timesince.days))
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user_list = [[movie, rating, date, movie_avg, user_avg, movie_time]]
        current_user = user
if user == current_user:
    datelist = sorted(user_list, key=lambda x: x[2])
    for i in range(0, len(datelist)):
        movieid = datelist[i][0]
        rating = datelist[i][1]
        movie_avg = datelist[i][3]
        user_avg = datelist[i][4]
        movie_time = datelist[i][5]
        # reformat date back to original YYYY-MM-DD
        date = datelist[i][2].isoformat()[0:10]
        if i == 0:
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movieid, current_user, rating, date, movie_avg, user_avg, movie_time, 0)
        else:
            # calculate the timedelta, use .days attribute to get days
            timesince = (datelist[i][2] - datelist[i-1][2])
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (movieid, current_user, rating, date, movie_avg, user_avg, movie_time, math.sqrt(timesince.days))