#!/usr/bin/env python
import sys, csv
""" input: Mapped data, must run on hadoop with
    -file path/to/movie_averages.txt#movie_averages.txt,path/to/user_averages.txt#user_averages.txt
    output: training set with movie_total averages appended"""
sys.path.append('.')
movie_dic = {}
user_dic = {}
with open('movie_averages.txt', 'rb') as data:
    reader = csv.reader(data, delimiter = '\t')
    for line in reader:
        movie_dic[line[0]] = line[1]
with open('user_averages.txt', 'rb') as data:
    reader = csv.reader(data, delimiter = '\t')
    for line in reader:
        user_dic[line[0]] = line[1]
for line in sys.stdin:
    fields = line.strip().split("\t")
    movie_avg = movie_dic[fields[0]]
    user_avg =  user_dic[fields[1]]
    print '%s\t%s\t%s\t%s\t%s\t%s' % (fields[0], fields[1], fields[2], fields[3], movie_avg , user_avg)
