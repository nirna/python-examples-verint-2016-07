""" write interlaced lines from input files 1 & 2 into the output file 3 """
import sys
from itertools import izip_longest
(_, file_input_1, file_input_2, file_output) = sys.argv
with open(file_input_1, 'r') as fin1:
    with open(file_input_2, 'r') as fin2:
        with open(file_output,'w') as fout:
            for line1,line2 in izip_longest(fin1, fin2, fillvalue=""):
                fout.write(str(line1) + str(line2))
