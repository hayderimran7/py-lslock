#!/usr/bin/env python
""" test file to create locks in given directory"""
import fcntl
import os
import sys

if len(sys.argv) < 3:
	print ("ERROR Running program")
	sys.exit("Usage: ./test-py-lslock <directory> <iterations>")
directory = sys.argv[1]
iterations = sys.argv[2]
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(int(iterations)):
    filename = '%s/%s.lock' % (directory, i)
    # Lock file
    f = open(filename, 'w')
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)