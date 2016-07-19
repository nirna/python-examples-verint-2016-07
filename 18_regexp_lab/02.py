import re

def toCamelCase(underscore_line):
    return re.sub(r'_(\w)', lambda m: m.group(0)[1].upper(), underscore_line)
