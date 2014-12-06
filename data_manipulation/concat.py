import sys
import random
import glob

fnames = glob.glob("./*_training.txt")

for fname in fnames:
    file = open(fname)
    for line in file:
    	print line.strip()



