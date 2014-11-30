#!/usr/bin/env python
import sys
import random
""" Emits the post-2005 portion of the mapped data, need to use
    training_set_sample_reducer_first.py as mapper instead of
    hadoop.IdentityMapper """

for line in sys.stdin:
    # populate sample list with 100k obs
    fields = line.strip().split(',',1)
    if fields[0] == 'post':
        print '%s' % (fields[1])
