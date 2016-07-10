""" Get two file paths and append the first one to the second one """
import os
import sys
(_, filepath_to_append, filepath_to_append_to) = sys.argv
with open(filepath_to_append, "rt") as fsrc:
    with open(filepath_to_append_to, "at") as fdst:
        for line in fsrc:
            fdst.write(line)