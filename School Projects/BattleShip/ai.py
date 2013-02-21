####################################################################
# Created by Christopher Primerano on 21-02-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
####################################################################

from player import Player
import random
import time

class AI(Player):
    def __init__(self, board, difficulty):
        if enhancements:
            self._difficulty = difficulty
        else:
            self._difficulty = 0
        self._prev_shot = ()
        self._prev_was_hit = False
        self._direction = 0
        self._last = ()
        # setup list of possible moves
        self._moves = [(x,y) for y in range(board.get_size()) for x in range(board.get_size())]
        Player.__init__(self, board)

    def get_prev_was_hit(self):
        return self._prev_was_hit
        
    def set_prev_was_hit(self, hit):
        self._prev_was_hit = hit
        
    def next_direction(self):
        self._prev_shot = self._last
        self._direction += 1
        if self._direction >= 4:
            self._prev_was_hit = False
        self._direction %= 4
        
        
    def get_difficulty(self):
        return self._difficulty
        
    def set_difficulty(self, difficulty):
        if difficulty >= 0 and difficulty <= 1:
            self._difficulty = difficulty
            return True
        return False
    
    def get_move(self):
        # get a move from the AI using an algorithm dependant on the difficulty selected by the user
        # either random points (difficulty = 0)
        # or every second point for the board and then the remaining (difficulty = 1)
        if self._difficulty == 0:
			# if the previous shot was a hit then follow the ship until there is a miss on all 4 sides
            if self._prev_was_hit:
                if self._direction == 0 and (self._prev_shot[0] + 1, self._prev_shot[1]) in self._moves:
                    self._prev_shot = (self._prev_shot[0] + 1, self._prev_shot[1])
                    self._moves.remove(self._prev_shot)
                    time.sleep(0.3)
                    return self._prev_shot
                elif self._direction == 1 and (self._prev_shot[0] - 1, self._prev_shot[1]) in self._moves:
                    self._prev_shot = (self._prev_shot[0] - 1, self._prev_shot[1])
                    self._moves.remove(self._prev_shot)
                    time.sleep(0.3)
                    return self._prev_shot
                elif self._direction == 2 and (self._prev_shot[0], self._prev_shot[1] + 1) in self._moves:
                    self._prev_shot = (self._prev_shot[0], self._prev_shot[1] + 1)
                    self._moves.remove(self._prev_shot)
                    time.sleep(0.3)
                    return self._prev_shot
                elif self._direction == 3 and (self._prev_shot[0], self._prev_shot[1] - 1) in self._moves:
                    self._prev_shot = (self._prev_shot[0], self._prev_shot[1] - 1)
                    self._moves.remove(self._prev_shot)
                    time.sleep(0.3)
                    return self._prev_shot
                else:
                    self.next_direction()
                    return self.get_move()
            i = random.randint(0, len(self._moves) - 1)
            self._prev_shot = self._moves[i]
            self._last = self._prev_shot
            self._moves.pop(i)
            # have the game sleep for 0.3 seconds to allow the human user to view the AI make its move
            # also to make it look like its thinking about where to go
            time.sleep(0.3)
            return self._prev_shot
        elif self._difficulty == 1:
            if self._prev_shot == ():
                self._prev_shot = (0,0)
                self._moves.remove((0,0))
                self._last = (0,0)
                return (0,0)
            else:
				# if the previous shot was a hit then follow the ship until there is a miss on all 4 sides
                if self._prev_was_hit:
                    if self._direction == 0 and (self._prev_shot[0] + 1, self._prev_shot[1]) in self._moves:
                        self._prev_shot = (self._prev_shot[0] + 1, self._prev_shot[1])
                        self._moves.remove(self._prev_shot)
                        time.sleep(0.3)
                        return self._prev_shot
                    elif self._direction == 1 and (self._prev_shot[0] - 1, self._prev_shot[1]) in self._moves:
                        self._prev_shot = (self._prev_shot[0] - 1, self._prev_shot[1])
                        self._moves.remove(self._prev_shot)
                        time.sleep(0.3)
                        return self._prev_shot
                    elif self._direction == 2 and (self._prev_shot[0], self._prev_shot[1] + 1) in self._moves:
                        self._prev_shot = (self._prev_shot[0], self._prev_shot[1] + 1)
                        self._moves.remove(self._prev_shot)
                        time.sleep(0.3)
                        return self._prev_shot
                    elif self._direction == 3 and (self._prev_shot[0], self._prev_shot[1] - 1) in self._moves:
                        self._prev_shot = (self._prev_shot[0], self._prev_shot[1] - 1)
                        self._moves.remove(self._prev_shot)
                        time.sleep(0.3)
                        return self._prev_shot
                    else:
                        self.next_direction()
                        return self.get_move()
                x = (self._last[0] + 2) % self._board.get_size()
                y = self._last[1] % self._board.get_size()
                y += (self._last[0] + 2) / self._board.get_size()
                if y >= self._board.get_size():
                    x += 1
                    y = 0
                while True:
                    if (x,y) in self._moves:
                        break
                    x = (x + 2)
                    y = y % self._board.get_size()
                    y += (x) / self._board.get_size()
                    x = x % self._board.get_size()
                    if y >= self._board.get_size():
                        x += 1
                        y = 0
                self._prev_shot = (x,y)
                self._last = (x,y)
                # have the game sleep for 0.3 seconds to allow the human user to view the AI make its move
                # also to make it look like its thinking about where to go
                time.sleep(0.3)
                self._moves.remove((x,y))
                return self._prev_shot
