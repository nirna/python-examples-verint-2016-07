import re

def toCamelCase(underscore_line):
    return re.sub(r'_(\w)', lambda m: m.group(0)[1].upper(), underscore_line)

def toUnderscoreCase(camel_line):
    return re.sub(r'([A-Z])', lambda m: '_' + m.group(0).lower(), camel_line)