import sys
import random
import glob

count = 0

limit = 10000
sample = []

fnames = glob.glob("./data_sample/by_month_dir/2004-11.txt")

for fname in fnames:
    file = open(fname)
    for line in file:
        if (count < limit):
            sample.append(line)
        else:
            val = random.randint(0,count-1)
            if (val < limit):
                sample[val] = line
        count +=1

for line in sample:
    print line.strip()

