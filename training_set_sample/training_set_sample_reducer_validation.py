#!/usr/bin/env python
import sys
""" Emits the validation portion of the mapped data """
for line in sys.stdin:
    fields = line.strip().split(',',1)
    if fields[0] == 'validation':
        print '%s' % (fields[1])
