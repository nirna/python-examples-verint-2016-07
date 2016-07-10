""" write interlaced lines from input files 1 & 2 into the output file 3 """
import sys
(_, file_input_1, file_input_2, file_output) = sys.argv
with open(file_input_1, 'r') as fin1:
    with open(file_input_2, 'r') as fin2:
        with open(file_output,'w') as fout:
            line1 = fin1.readline()
            line2 = fin2.readline()
            while line1 + line2 != "":
                fout.write(line1 + line2)
                line1 = fin1.readline()
                line2 = fin2.readline()
