""" return a sub-list of words that are longer than the threshold argument """

def longer_than(length_thresh, *words):
    return [w for w in words if type(w)==str and len(w)>length_thresh]

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')