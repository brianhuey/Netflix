#!/usr/bin/env python
import sys, datetime, math
""" Create dictionary with user as a key, sort by date and
    calculate the time since the user was last rated """
current_user = None
user_list = []
for line in sys.stdin:
    user, movie, rating, date = line.strip().split("\t", 3)
    if current_user == user:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user_list.append([movie,rating,date])
    else:
        if current_user:
            datelist = sorted(user_list, key=lambda x: x[2])
            for i in range(0, len(datelist)):
                movieid = datelist[i][0]
                rating = datelist[i][1]
                # reformat date back to original YYYY-MM-DD
                date = datelist[i][2].isoformat()[0:10]
                if i == 0:
                    print '%s\t%s\t%s\t%s\t%s' % (user, movieid, rating, date,0)
                else:
                    # calculate the timedelta, use .days attribute to get days
                    timesince = (datelist[i][2] - datelist[i-1][2])
                    print '%s\t%s\t%s\t%s\t%s' % (user, movieid, rating, date, math.sqrt(timesince.days))
        user_list = []
        current_user = user
