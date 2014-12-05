import sys
import random
import glob

count = 0

limit = 1000
u_sample = []
m_sample = []

def update_sample(sample,count,limit,line):
    if (count < limit):
        sample.append(line)
    else:
        val = random.randint(0,count-1)
        if (val < limit):
            sample[val] = line

for line in sys.stdin:
    fields = line.strip().split(",")
    update_sample(u_sample,count,limit,fields[1])
    update_sample(m_sample,count,limit,fields[0])
    count +=1

def permute(sample,count):
    for i in range(1,count):
        val = random.randint(0,i-1)
        swap = sample[val]
        sample[val] =sample[i]
        sample[i] = swap

permute(u_sample,count)
permute(m_sample,count)

for i in range(0,count):
    print "%s,%s" % (m_sample[i],u_sample[i])




