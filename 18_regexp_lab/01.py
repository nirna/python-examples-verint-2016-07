import sys
import re

cfg_file_path = sys.argv[1]
key_in = sys.argv[2]
with open(cfg_file_path, 'r') as cfg_file:
    for line in cfg_file:
        res = re.search(r'^\s*'+key_in+r'\s*=\s*(.*)$', line)
        if res is not None:
            return res.group(1)
