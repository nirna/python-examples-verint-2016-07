""" Return IPs from hosts file per input machine name(s) """
import sys
from collections import defaultdict
# Read input args
host_file_path, pc_names = sys.argv[1], sorted(sys.argv[2:])
# Read hosts into a dictionary
dict_hosts = defaultdict(lambda: "No IP")
with open(host_file_path,'r') as fin:
    for line in fin: 
        (host_name, host_ip) = line.rstrip().split("=")
        dict_hosts[host_name] = host_ip

# Print results
max_length = max(len(pc_name) for pc_name in pc_names)
for pc_name in pc_names: print "%-*s: %s" % (max_length, pc_name, dict_hosts[pc_name])
