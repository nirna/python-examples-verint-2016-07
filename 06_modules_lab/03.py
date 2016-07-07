""" 
Delete large files (larger from 1MB by default) from specified folder (default is \) 
"""
#Week01_Exercise02_Assignment03
import os
import sys
# Read input arguments
root_dir, size_threshold_bytes = '\\', 1024*1024
if len(sys.argv) > 1: root_dir = sys.argv[1]
if len(sys.argv) > 2: size_threshold_bytes = int(sys.argv[2])
# Traverse files and delete large files
for name in os.listdir(root_dir):
    filepath = root_dir  + name
    if os.path.isfile(filepath) and os.path.getsize(filepath) > size_threshold_bytes :
        print "Deleting large file [%d Bytes]: %s" % (os.path.getsize(filepath), filepath)
        os.remove(filepath)
