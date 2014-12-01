#!/usr/bin/env python
import sys
""" Subsets training set by month """
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
# open files corresponding to each month
files = [open('%s_training.txt' %s, 'w') for s in months]
for line in sys.stdin:
    # populate sample list with 100k obs
    movie, user, rating, date = line.strip().split(",",3)
    date_str = str(date[5:7])
    if date_str[0] == '0':
        index = int(date_str[-1])-1
        final_line = line.strip() + str('\n')
        # write to the appropriate file
        files[index].write(final_line)
    else:
        index = int(date_str)-1
        final_line = line.strip() + str('\n')
        files[index].write(final_line)
for i in files:
    files[i].close()