""" 
Delete large files (larger from 1MB by default) from specified folder (default is \) 
"""
#Week01_Exercise02_Assignment03_bonus
import os
import sys
import argparse
# Read input arguments
parser = argparse.ArgumentParser()
parser.add_argument("root_dir", 
                    type=str,
                    default=os.path.abspath(os.sep),
                    help="The root folder to search under")
parser.add_argument("size_threshold_bytes", 
                    type=int,
                    default=1024*1024,
                    help="The threshold of the file size in bytes; larger files will be removed")
args = parser.parse_args()
# Traverse files and delete large files
for name in os.listdir(args.root_dir):
    filepath = args.root_dir + os.sep + name
    if os.path.isfile(filepath) and os.path.getsize(filepath) > args.size_threshold_bytes :
        print "Deleting large file [%d Bytes]: %s" % (os.path.getsize(filepath), filepath)
        os.remove(filepath)