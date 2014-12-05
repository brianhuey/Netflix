import sys
import random
import glob

count = 0
pair_file_name = sys.argv[1]

#print pair_file_name
pair_file = open(pair_file_name)

pairs  ={}
for line in pair_file:
    fields = line.strip().split(",")
    pairs[(fields[0],fields[1])] = 0


test_size = 0
for line in sys.stdin:
    fields = line.strip().split(",")
    test_size += 1
    #print fields
    if (fields[0],fields[1]) in pairs:
        pairs[(fields[0],fields[1])] +=1 

hits = 0
for key in pairs.keys():
    hits += pairs[key]

out_of = len(pairs.keys())

print("%d true positives" % hits)
print("%d false positives" % (out_of - hits))
print("%d false negative" % (test_size - hits))


                  
