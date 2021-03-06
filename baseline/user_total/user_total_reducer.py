#!/usr/bin/env python
import sys
""" Create dictionary with number of movies rated for each user,
	and total number of ratings
    Output: number of movies rated, total: total number of movie ratings"""
user_dic = {'total users': 0}
for line in sys.stdin:
    fields = line.strip().split("\t")
    if fields[0] in user_dic:
    	user_dic[fields[0]] += 1
    else:
    	user_dic[fields[0]] = 1
        user_dic['total users'] += 1
for key in user_dic:
	print '%s\t%s' % (key, user_dic[key])
