from lib.player import Player
from random import randint

"""
start(p1, p2) - starts a new game with players p1 and p2

play(row,column) - current player picked a square. If the square was free mark it as X or O and switch turns to the other player.
If square was taken or not in the board, or game is over, raise an exception.

winner() - If game is over return the winning player, else return None

val(row, column) - return current value for square (X, O or empty)
"""

class InvalidMove(Exception):
    def __init__(self,msg):
        self.message = "Invalid move in a tick-tack-toe; %s" %(msg)


class Game:
    def __init__(self):
        self.reset_board()
        self.players = [None,None]
        self.current_player = None
        self.winner = None
        self.moves_counter = 0
    
    def reset_board(self):
        self.data = [ [None,None,None] , 
                      [None,None,None] , 
                      [None,None,None] ]
    
    """ start(p1, p2) - starts a new game with players p1 and p2 """
    def start(self, p1, p2):
        #if (type(p1) is not Player) or (type(p2) is not Player): raise ValueError("Input must be of type Player")
        self.moves_counter = 0
        self.reset_board()
        self.players[0] = p1
        self.players[1] = p2
        self.current_player = self.players[self.moves_counter % 2]
        self.winner = None

    """ play(row,column) - current player picked a square. If the square was free mark it as X or O and switch turns to the other player.
    If square was taken or not in the board, or game is over, raise an exception. """
    def play(self, row, column):
        if not (0<=row<=2 and 0<=column<=2): raise InvalidMove("Row/Col must be integers between 0 and 2")
        if self.data[row][column] is not None: raise InvalidMove("Cell already occupied")
        if self.winner is not None: raise InvalidMove("Game Over")
        self.data[row][column] = self.current_player
        self.moves_counter += 1
        self.current_player = self.players[self.moves_counter % 2]
        self.checkwinner()

    def tie(self):
        if (self.moves_counter >= 9) and (self.winner is None): return True # Game over and no winner
        return False

    def checkwinner(self):
        if   self.data[0][0] == self.data[0][1] == self.data[0][2] != None: self.winner = self.data[0][0] # Row 0
        elif self.data[1][0] == self.data[1][1] == self.data[1][2] != None: self.winner = self.data[1][0] # Row 1
        elif self.data[2][0] == self.data[2][1] == self.data[2][2] != None: self.winner = self.data[2][0] # Row 2
        elif self.data[0][0] == self.data[1][0] == self.data[2][0] != None: self.winner = self.data[0][0] # Col 0
        elif self.data[0][1] == self.data[1][1] == self.data[2][1] != None: self.winner = self.data[0][1] # Col 1
        elif self.data[0][2] == self.data[1][2] == self.data[2][2] != None: self.winner = self.data[0][2] # Col 2
        elif self.data[0][0] == self.data[1][1] == self.data[2][2] != None: self.winner = self.data[1][1] # Left diagonal
        elif self.data[2][0] == self.data[1][1] == self.data[0][2] != None: self.winner = self.data[1][1] # Right diagonal

    """ val(row, column) - return current value for square (X, O or empty) """
    def val(self, row, column):
        return self.data[row][column].marker if (self.data[row][column] is not None) else " "

    def __str__(self):
        board_str = ""
        for r in range(3):
            board_str += "\n-------\n|"
            for c in range(3):
                board_str += self.val(r,c) + "|"
        board_str += "\n-------\n"
        return board_str
