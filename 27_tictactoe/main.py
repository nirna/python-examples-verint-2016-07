import re
import lib.board as board
from lib.player import Player

players = [None,None]
i = 0

while True:

    # Get players' info
    while i < 2:
        try:
            players[i] = Player(name   = raw_input("Player %d - Name:   " %(i)),
                                marker = raw_input("Player %d - Marker: " %(i)))
            i += 1
        except Exception as e:
            print "Error occured while setting player %d\nError message: %s" %(i, e.message)


    # Init game
    tto = board.Game()
    tto.start(players[0], players[1])

    # Play game
    while (tto.winner is None) and (not tto.tie()):
        current_play = raw_input("%s's play (enter row,col): " % tto.current_player.name)
        m = re.search(r'^\s*(\w)[,;\s\.]*(\w)\s*$', current_play)
        try:
            tto.play(int(m.group(1)),int(m.group(2)))
            print tto
        except board.InvalidMove as e:
            print e.message
        except Exception as e:
            print e.message

    # Print results
    if tto.tie(): print "Game tied!!"
    else: print "Winner is %s - well done!!\n" %(tto.winner.name)
    print "------- GAME OVER --------\n"

    # Continue?
    if raw_input("Would you like to play again (y/n)? ").lower() == 'n': 
        print "\nGood bye... Hope you enjoyed!!\n"
        break
    if raw_input("Same players (y/n)? ").lower() == 'n': 
        i = 0
