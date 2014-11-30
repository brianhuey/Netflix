#!/usr/bin/env python
import sys, datetime
""" Create dictionary with user as a key, sort by date and
    calculate the time since the user was last rated """
user_dic = {}
for line in sys.stdin:
    user, movie, rating, date = line.strip().split("\t", 3)
    if user in user_dic:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user_dic[user].append([movie, rating, date])
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user_dic[user] = [[movie, rating, date]]
for key in user_dic:
    # sort by date index
    datelist = sorted(user_dic[key], key=lambda x: x[2])
    for i in range(0, len(datelist)):
        movieid = datelist[i][0]
        rating = datelist[i][1]
        # reformat date back to original YYYY-MM-DD
        date = datelist[i][2].isoformat()[0:10]
        if i == 0:
            print '%s\t%s\t%s\t%s\t%s' % (movieid, key, rating, date, 0)
        else:
            # calculate the timedelta, use .days attribute to get days
            timesince = (datelist[i][2] - datelist[i-1][2])
            print '%s\t%s\t%s\t%s\t%s' % (movieid, key, rating, date, timesince.days)
