#!/usr/bin/env python
import sys
""" Create dictionary with number of user ratings for each movie,
    and total number of ratings
    Input: training_set_reshape.txt
    Output: number of ratings by movie, total: total number of user ratings"""

movie_dic = {'total movies': 0}

for line in sys.stdin:
    fields = line.strip().split("\t")
    #print fields
    if fields[0] in movie_dic:
    	movie_dic[fields[0]] += 1
    else:
    	movie_dic[fields[0]] = 1
        movie_dic['total movies'] += 1

for key in movie_dic:
	print '%s\t%s' % (key, movie_dic[key])



