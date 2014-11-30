import sys
import glob


prefix = "by_month_dir/"

output_pairs = []

for year in xrange(1999,2006):
    for month in xrange(0,13):
        grep_str = str(year)
        if (month < 10):
            grep_str += "-0%d" % month
        else:
            grep_str += "-%d" % month
        filename = grep_str+".txt"
        output_pairs.append((filename,grep_str,open(prefix+filename,"w")))

fnames = glob.glob("./training_set/*.txt")

for fname in fnames:
    file = open(fname)
    for line in file:
        fields = line.strip().split(",")
        #print fields
        for x in output_pairs:
            if x[1] in fields[3]:
                #print "Putting ", line, " in file ", x[0]
                print >> x[2], line.strip()
            

for x in output_pairs:
    x[2].close()
