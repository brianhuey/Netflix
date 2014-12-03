#!/usr/bin/env python
import sys, datetime, math
""" Input: Training set with global averages appended
    Calculates the time since the movie was last rated
    Output: sqrt(time last rated)"""
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
            for i in range(0, len(datelist)):
                userid = datelist[i][0]
                rating = datelist[i][1]
                movie_avg = datelist[i][3]
                user_avg = datelist[i][4]
                # parse out timestamp reformat date back to original YYYY-MM-DD
                date = datelist[i][2].isoformat()[0:10]
                if i == 0:
                    print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_movie, userid, rating, date, movie_avg, user_avg, 0)
                else:
                    # calculate the timedelta, use .days attribute to get days
                    timesince = (datelist[i][2] - datelist[i-1][2])
                    print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_movie, userid, rating, date, movie_avg, user_avg, math.sqrt(timesince.days))
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        movie_list = [[user,rating,date,movie_avg,user_avg]]
        current_movie = movie
# On last line, emit the contents of the final list
if movie == current_movie:
    datelist = sorted(movie_list, key=lambda x: x[2])
    for i in range(0, len(datelist)):
        userid = datelist[i][0]
        rating = datelist[i][1]
        movie_avg = datelist[i][3]
        user_avg = datelist[i][4]
        # reformat date back to original YYYY-MM-DD
        date = datelist[i][2].isoformat()[0:10]
        if i == 0:
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_movie, userid, rating, date, movie_avg, user_avg, 0)
        else:
            # calculate the timedelta, use .days attribute to get days
            timesince = (datelist[i][2] - datelist[i-1][2])
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_movie, userid, rating, date, movie_avg, user_avg, math.sqrt(timesince.days))
