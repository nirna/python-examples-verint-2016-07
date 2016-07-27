"""
Write a program that takes a file name
and prints line count for the file

Alert the user politely if there was any problem opening the file
"""
import os
import argparse

# Define input arguments
parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=str, help="The file path to count lines of.")

# Read input arguments
args = parser.parse_args()

try:
    if not os.path.exists(args.file_path):
        raise Exception("File not found")

    with open(args.file_path,'r') as fin:
        counter = 0
        for _ in fin: counter += 1
        print "Line count is %d" % counter

except Exception as e:
    print "Error ocured while trying to open file \"%s\".\nError message: %s" % (args.file_path,e.message)
