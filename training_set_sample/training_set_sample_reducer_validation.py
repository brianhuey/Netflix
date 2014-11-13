#!/usr/bin/env python
import sys
import random
""" Emits the validation portion of the mapped data """

for line in sys.stdin:
    # populate sample list with 100k obs
    fields = line.strip().split(',',1)
    if fields[0] == 'validation':
        print '%s' % (fields[1])
