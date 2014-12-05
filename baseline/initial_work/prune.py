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
    pairs[(fields[0],fields[1])] = True

for line in sys.stdin:
    fields = line.strip().split(",")
    #print fields
    if (fields[0],fields[1]) in pairs:
        pairs[(fields[0],fields[1])] = False

for key in pairs.keys():
    if pairs[key]:
        print "%s,%s" % (key[0],key[1])
                  
