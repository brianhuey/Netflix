import numpy as np
import csv

def scale_3_by_4_file(filename, outfile_name="scaled.out" ):

    f = open(filename)
    
    outfile = open(outfile_name,"w")
    
    for line in f:

        fields = line.strip().split(',')

        print >> outfile, ("%s,%s,%f") % (fields[0], fields[1], ((float(fields[2]))/(float(fields[3]))))
        
    outfile.close()

