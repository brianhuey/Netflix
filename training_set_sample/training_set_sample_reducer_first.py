#!/usr/bin/env python
import sys
""" Emits the validation portion of the mapped data """

for line in sys.stdin:
    # populate sample list with 100k obs
    print '%s' % (line.strip())
