import re
import sys

input_csv = sys.argv[1]
with open(input_csv) as fin:
    for line in fin:
        print re.sub(r'^([^,]*),([^,]*),', lambda m: m.group(2) + ',' + m.group(1) + ',', line.strip())
