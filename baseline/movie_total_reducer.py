#!/usr/bin/env python
import sys
""" Create dictionary with average number of user ratings for each movie,
    and total number of ratings
    Input: training_set_reshape.txt
    Output: moviex: number of user ratings, total: total number of user ratings"""

movie_dic = {'total movies': 1}

for line in sys.stdin:
    fields = line.strip().split(",")
    #print fields
    if fields[0] in movie_dic:
    	movie_dic[fields[0]] += 1
    	movie_dic['total movies'] += 1
    else:
    	movie_dic[fields[0]] = 1

for key in movie_dic:
	print '%s,%s' % (key, movie_dic[key])



