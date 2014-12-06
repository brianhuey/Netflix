import sys

for line in sys.stdin:
    fields = line.strip().split(",")

    print "%s,%s,%f" % (fields[0],fields[1],float(fields[2])/float(fields[3]))

    
