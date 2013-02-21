####################################################################
# Created by Christopher Primerano on 21-02-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
####################################################################

from player import Player
import pygame

class User(Player):
    def __init__(self, board, side):
        # side is either 0 (left), or 1 (right)
        self._side = side
        self._moves = []
        Player.__init__(self, board)

    def get_prev_was_hit(self):
        return False
        
    def set_prev_was_hit(self, hit):
        pass
        
    def get_side(self):
        return self._side
        
    def set_side(self, side):
        if side >= 0 and side <= 1:
            self._side = side
            return True
        return False
        
    def get_move(self):
        # if enhancements are enabled get the co-ordinates of the users mouse click and convert it into a valid move
        if enhancements:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        x = event.pos[0]
                        y = event.pos[1] - 50
                        x = x / 11
                        y = y / 11
                        # account for the player's board being on a certain side of the game board
                        if self._side == 1:
                            if x >= 0 and x <= 9 and y <= 9:
                                if (x,y) in self._moves:
                                    continue
                                self._moves.append((x,y))
                                return (x,y)
                        else:
                            if x > 9 and y <= 9:
                                if (x,y) in self._moves:
                                    continue
                                self._moves.append((x,y))
                                return (x-10,y)
        else:
            # if enhancements are not enabled ask the user for co-ordinates to attack and check to make sure they are a valid move
            valid = False
            output = ()
            while(not valid):
                input = raw_input("Please enter co-ordinates of where you would like to attack 'x, y': ")
                values = input.split(",")
                # check to make sure the user has imput 2 values for the co-ordinates
                if len(values) == 2:
                    x = values[0].strip()
                    y = values[1].strip()
                    # try to convert the co-ordinates to integers, if not possible then ask for new co-ordinates
                    try:
                        x = int(x)
                        y = int(y)
                        # if co-ordinates are integers but are illegal values (outside of the board) then ask for new ones
                        if x > self._board._size or y > self._board._size or x < 0 or y < 0:
                            print "Your input was outside of the field."
                            continue
                        # do not allow the user to make the same move twice
                        if (x,y) in self._moves:
                            raise ValueError
                        valid = True
                        self._moves.append((x,y))
                        output = (x,y)
                    except ValueError:
                        print "your input was invalid, please try again."
                else:
                    print "your input was invalid, please try again."
            return output
