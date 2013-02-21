#!/usr/bin/env python
from game import Game

# used to toggle enhancements, has no other effect on how the game actually runs
import __builtin__
__builtin__.enhancements = True

if __name__ == "__main__":
    # create a new game instance
    g = Game()
    # start the new game
    g.start()
