import sys
import random
import glob
""" Samples 100,000 observations from the training set to
    create a validation set that matches the size of the
    KDD-provided test set. In addition we output the remaining
    observations as the training set """
count = 0
limit = 100
# validation set
sample = []
# remainder is training set
training = []
fnames = glob.glob("../training_set_reshape/training_set_1000.txt")

for fname in fnames:
    file = open(fname)
    size = 1000 # Calculated using 'wc -l training_set_reshape.txt'
    for line in file:
        # populate sample list with 100k obs
        val = random.randint(0, size)
        if (val < limit):
            sample.append(line)
        # once sample is populated, generate random number
        else:
            training.append(line)

for line in sample:
    print '%s,%s' % ('validation', line.strip())

for line in training:
    print '%s,%s' % ('training', line.strip())


