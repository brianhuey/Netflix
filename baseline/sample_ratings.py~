import sys
import random
import glob

count = 0
if len(argv) > 1:
    users = True
limit = 1000
sample = []


for line in os.stdin:
    if (count < limit):
        sample.append(line)
    else:
            val = random.randint(0,count-1)
            if (val < limit):
                sample[val] = line
        count +=1

count = 0

for line in sample:
    foo = line.strip().split(",")
    if (users):
        print count, foo[1]
    else:
        print count, foo[0]
    count +=1

        
