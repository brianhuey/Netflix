import sys
import random
import glob

count = 0

limit = 1000
sample = []

fnames = glob.glob("training_set_w_mid/*.txt")

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
