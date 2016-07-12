""" Find anagrams in word list (read from a file) """
import sys
from collections import Counter
# Read input args
anagrams_file_path = sys.argv[1]
# Read words into a dictionary holding their histogram as key
dict_anagrams = {}
with open(anagrams_file_path,'r') as fin:
    for word in fin: 
        # Generate a sorted lower case letters histogram
        word = word.rstrip().lower()
        sorted_dict_letters = ""
        dict_letters = Counter(word)
        for k in sorted(dict_letters): sorted_dict_letters += k + str(dict_letters[k])
        # Add words to dictionary with their histogram as key
        if dict_anagrams.has_key(sorted_dict_letters): dict_anagrams[sorted_dict_letters].append(word)
        else: dict_anagrams[sorted_dict_letters] = [word]

# Print results
for hist in dict_anagrams: print dict_anagrams[hist]
