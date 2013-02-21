####################################################################
# Created by Christopher Primerano on 21-02-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
# the Player class should never be directly instantiated           #
####################################################################

import board

class Player:
    def __init__(self, board):
        self._board = board
    
    def get_board(self):
        return self._board
    
    def set_board(self, board):
        self._board = board
        return True
    
    def is_hit(self, point):
        return self._board.is_hit(point)
    
    def is_defeated(self):
        return self._board.is_defeated()
    
    def get_move(self):
        return (0,0)
    
    def get_ships_left(self):
        return self._board.get_ships_left()
	
