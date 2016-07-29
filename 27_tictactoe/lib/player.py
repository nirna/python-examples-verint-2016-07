
class Player:

    def __init__(self, name, marker):
        if type(name)!=str: raise ValueError('Player name must be a string')
        self.name = name
        if type(marker)!=str or len(marker)!=1: raise ValueError('Player marker must be a single character')
        self.marker = marker

    def __str__(self):
        return self.marker