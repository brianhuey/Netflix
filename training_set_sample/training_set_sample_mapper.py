#!/usr/bin/env python
import sys, random
""" Maps 100,000 observations from the training set to
    create a validation set that matches the size of the
    KDD-provided test set. In addition we output the remaining
    observations as the training set """
limit = 100000
size = 100480507 # Calculated using 'wc -l training_set_reshape.txt'
for line in sys.stdin:
    # populate sample list with 100k obs
    val = random.randint(0, size)
    if val < limit:
        print '%s,%s' % ('validation', line.strip())
    # once sample is populated, generate random number
    else:
        print '%s,%s' % ('training', line.strip())
