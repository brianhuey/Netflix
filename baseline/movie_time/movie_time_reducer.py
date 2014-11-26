#!/usr/bin/env python
import sys, datetime
""" Create dictionary with movie as a key, sort by date and
    calculate the time since the movie was last rated"""

movie_dic = {}
for line in sys.stdin:
    movie, user, rating, date = line.strip().split("\t", 3)
    if movie in movie_dic:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    	movie_dic[movie].append([user,rating,date])
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    	movie_dic[movie] = [[user,rating,date]]

for key in movie_dic:
    # sort by date index
    datelist = sorted(movie_dic[key], key=lambda x: x[2])
    for i in range(0,len(datelist)):
        userid = movie_dic[key][i][0]
        rating = movie_dic[key][i][1]
        # reformat date back to original YYYY-MM-DD
        date = movie_dic[key][i][2].isoformat()[0:10]
        if i == 0:
            print '%s\t%s\t%s\t%s\t%s' % (key,userid,rating,date,0)
        else:
            # calculate the timedelta, use .days attribute to get days
            timesince = (datelist[i][2] - datelist[i-1][2])
            print '%s\t%s\t%s\t%s\t%s' % (key,userid,rating,date,timesince.days)



