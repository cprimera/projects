####################################################################
# Created by Christopher Primerano on 21-02-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
####################################################################

import random
from point import Point
from ship import Ship
from PIL import Image, ImageDraw
import pygame

class Board:
    def __init__(self, size=10, ship_2_size=1, ship_3_size=2, ship_4_size=1, ship_5_size=1):
        self._size = size
        self._spots = {}
        # setup points for the board and check to make sure they were setup properly
        for i in range(self._size):
            for j in range(self._size):
                p = Point(0, (j,i))
                self._spots[j,i] = p
        for i in range(self._size):
            for j in range(self._size):
                if self._spots[j,i].get_state() != 0:
                    print "Error in initial state"
        # setup the ships of each size, the ships are placed randomly, if they ships will not completely fit after 10000 tries per ship
        # the game will stop trying to place ships of that size and move on to the next size
        self._ship2 = []
        i = 0
        tries = 0
        while i < ship_2_size:
            if tries >= 10000:
                print "You need to change the board size or the number of ships"
                break
            orientation = random.randint(0,1)
            randomx = random.randint(0, self._size-1 - (((orientation + 1) % 2) * 2))
            randomy = random.randint(0, self._size-1 - (orientation * 2))
            points = []
            spot_taken = False
            for j in range(2):
                if self._spots[randomx + (j * ((orientation + 1) % 2)),randomy + (j * orientation)].get_state() == 4:
                    spot_taken = True
                    break
            if spot_taken:
                tries += 1
                continue
                
            for j in range(2):
                points.append(self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)])
                self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)].set_state(4)
            self._ship2.append(Ship(self._spots[randomx,randomy], 2, orientation, points))
            i += 1
        self._ship3 = []
        i = 0
        tries = 0
        while i < ship_3_size:
            if tries >= 10:
                print "You need to change the board size or the number of ships"
                break
            orientation = random.randint(0,1)
            randomx = random.randint(0, self._size-1 - (((orientation + 1) % 2) * 3))
            randomy = random.randint(0, self._size-1 - (orientation * 3))
            points = []
            spot_taken = False
            for j in range(3):
                if self._spots[randomx + (j * ((orientation + 1) % 2)),randomy + (j * orientation)].get_state() == 4:
                    spot_taken = True
                    break
            if spot_taken:
                tries += 1
                continue
                
            for j in range(3):
                points.append(self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)])
                self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)].set_state(4)
            self._ship3.append(Ship(self._spots[randomx,randomy], 3, orientation, points))
            i += 1
        self._ship4 = []
        i = 0
        tries = 0
        while i < ship_4_size:
            if tries >= 10:
                print "You need to change the board size or the number of ships"
                break
            orientation = random.randint(0,1)
            randomx = random.randint(0, self._size-1 - (((orientation + 1) % 2) * 4))
            randomy = random.randint(0, self._size-1 - (orientation * 4))
            points = []
            spot_taken = False
            for j in range(4):
                if self._spots[randomx + (j * ((orientation + 1) % 2)),randomy + (j * orientation)].get_state() == 4:
                    spot_taken = True
                    break
            if spot_taken:
                tries += 1
                continue
                
            for j in range(4):
                points.append(self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)])
                self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)].set_state(4)
            self._ship4.append(Ship(self._spots[randomx,randomy], 4, orientation, points))
            i += 1
        self._ship5 = []
        i = 0
        tries = 0
        while i < ship_5_size:
            if tries >= 10:
                print "You need to change the board size or the number of ships"
                break
            orientation = random.randint(0,1)
            randomx = random.randint(0, self._size-1 - (((orientation + 1) % 2) * 5))
            randomy = random.randint(0, self._size-1 - (orientation * 5))
            points = []
            spot_taken = False
            for j in range(5):
                if self._spots[randomx + (j * ((orientation + 1) % 2)),randomy + (j * orientation)].get_state() == 4:
                    spot_taken = True
                    break
            if spot_taken:
                tries += 1
                continue
                
            for j in range(5):
                points.append(self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)])
                self._spots[randomx+(j * ((orientation + 1) % 2)),randomy+(j * orientation)].set_state(4)
            self._ship5.append(Ship(self._spots[randomx,randomy], 5, orientation, points))
            i += 1
            
    def get_ships_left(self):
        ''' return the number of ships remaining (un-sunk) on the players board '''
        counter = 0
        for ship in self._ship2:
            if not ship.is_sunk():
                counter += 1
        for ship in self._ship3:
            if not ship.is_sunk():
                counter += 1
        for ship in self._ship4:
            if not ship.is_sunk():
                counter += 1
        for ship in self._ship5:
            if not ship.is_sunk():
                counter += 1
        return counter
            
    def get_size(self):
        return self._size
        
    def set_size(self, size):
        self._size = size
        return True
            
    def is_hit(self, point):
        ''' return if the point is a hit on the players board '''
        # check through the ships on the board to see if the point is a hit, if not set the state of the point to be a miss
        p = self._spots[point.get_point()]
        # could have simplified this as to just use the state of the point since it keeps track of
        # whether it is under a ship or not, but to be thourough we check with the ship also to 
        # make sure that it is actually a hit and the point hasn't just been tampered with
        if p.get_state() == 4:
            if self._ship2 != []:
                for ship in self._ship2:
                    if ship.is_hit(p):
                        return True
            if self._ship3 != []:
                for ship in self._ship3:
                    if ship.is_hit(p):
                        return True
            if self._ship3 != []:
                for ship in self._ship4:
                    if ship.is_hit(p):
                        return True
            if self._ship3 != []:
                for ship in self._ship5:
                    if ship.is_hit(p):
                        return True
            p.set_state(1)
            return False
        elif p.get_state() == 0:
            p.set_state(1)
            return False
        else:
            return False
            
    def is_defeated(self):
        ''' return True if all ships have been sunk on the players board '''
        output = True
        if self._ship2 != []:
            for ship in self._ship2:
                if not ship.is_sunk():
                    output = False
        if self._ship3 != []:
            for ship in self._ship3:
                if not ship.is_sunk():
                    output = False
        if self._ship4 != []:
            for ship in self._ship4:
                if not ship.is_sunk():
                    output = False
        if self._ship5 != []:
            for ship in self._ship5:
                if not ship.is_sunk():
                    output = False
        return output
        
    def draw_board(self, draw_ships):
        # create a PIL image of the board and convert to a pygame image for display
        # if draw_ships is set it will also draw the ships on the board
        image = Image.new("RGB", (self._size * 11,self._size * 11), "#00f")
        draw = ImageDraw.Draw(image)
        
        for i in range(self._size):
            p1 = ((i * 11) + 11, 0)
            p2 = ((i * 11) + 11, self._size * 11)
            box = [p1,p2]
            draw.rectangle(box, "#000")
            p1 = (0, (i * 11) + 11)
            p2 = (self._size * 11, (i * 11) + 11)
            box = [p1,p2]
            draw.rectangle(box, "#000")
            
        for point in self._spots.values():
            point.draw_point(image, draw, draw_ships)
            
        image = pygame.image.fromstring(image.tostring(), image.size, 'RGB')
        imagerect = image.get_rect()
                        
        return image, imagerect
        
    def __str__(self):
        # create a string output of the board
        output = ""
        for i in range(self._size):
            for j in range(self._size):
                output += str(self._spots[j,i]) + " "
            output += "\n"
        return output
