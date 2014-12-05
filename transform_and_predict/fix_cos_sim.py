
def fix_cos_sim(filename, dir_prefix="./filename."):

    f = open(filename)
    
    outfile = open(dir_prefix+"formatted","w")
    
    for line in f:

        fields = line.strip().split(',')

        print >> outfile, ("(%s,%s)\t%d") % (fields[0], fields[1], (fields[2]/fields[3]))
        
    outfile.close()
