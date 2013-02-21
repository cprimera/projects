#!/usr/bin/env python

####################################################################
# Created by Christopher Primerano on 21-02-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
####################################################################

from game import Game

# used to toggle enhancements, has no other effect on how the game actually runs
import __builtin__
__builtin__.enhancements = True

if __name__ == "__main__":
    # create a new game instance
    g = Game()
    # start the new game
    g.start()
