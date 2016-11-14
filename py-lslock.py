#!/usr/bin/env python
""" program to check locked files in a given directory
"""

import fnmatch
import os
import platform
import sys

class LsLock(object):
    """ Check files locked with flock and print them """
    def __init__(self, path):
        self.info = {}
        self.read_lock_files(path)
        self.search_proc_locks()

    def read_lock_files(self, path):
        """ For given path, read all files that end with .lock """
        # iterate all files in given path 
        for root, dirs, files in os.walk(path):
            for matched_file in fnmatch.filter(files, '*.lock'):
                filename = os.path.join(root, matched_file)
                # get inode of matched file
                inode = os.stat(filename).st_ino
                self.info.update({inode: {'file': filename}})

    def search_proc_locks(self):
        """ Get PID and inodes from /proc/locks file"""
        with open('/proc/locks', 'r') as proc_file:
            for line in proc_file.readlines():
                data = line.split(' ')
                data = filter(lambda x: x, data)
                pid = data[4]
                inode = int(data[5].split(':')[-1])
                if inode in self.info:
                    self.info[inode].update({'pid': pid})

    def __repr__(self):
        result = []
        for i, v in self.info.iteritems():
            result.append('{f}'.format(f=v.get('file')))
        return '\n'.join(result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("ERROR Running program")
        sys.exit("Usage: py-lslock <directory>")
    if platform.system().lower() not in ['linux','linux2']:
        print("System is not Linux, therefore /proc/locks doesnt exist")
        print ("Exiting ...")
        sys.exit(1)

    directory = sys.argv[1]
    inst = LsLock(directory)
    print ("result of all locked files found in directory %s " %directory)
    print("LOCKED_FILE")
    print(inst)
