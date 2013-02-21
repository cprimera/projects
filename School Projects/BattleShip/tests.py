####################################################################
# Created by Christopher Primerano on 21-02-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
####################################################################

import unittest
from point import Point
from ship import Ship
from player import Player
from user import User
from ai import AI
from board import Board
import __builtin__
__builtin__.enhancements = False

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(0, (0,0))
        
    def test_get_point(self):
        self.assertEqual(self.point.get_point(), (0,0))
                
    def test_set_point(self):
        self.assertEqual(self.point.set_point((0,1)), True)
        self.assertEqual(self.point._point, (0,1))
        
    def test_get_state(self):
        self.assertEqual(self.point.get_state(), 0)
                
    def test_set_state(self):
        self.assertEqual(self.point.set_state(1), True)
        self.assertEqual(self.point._state, 1)
        self.assertEqual(self.point.set_state(100), False)
        self.assertNotEqual(self.point._state, 100)
        
    def test_equal(self):
        self.assertEqual(self.point == Point(0, (0,0)), True)
        self.assertEqual(self.point == Point(1, (0,0)), True)
        self.assertEqual(self.point == Point(0, (1,1)), False)
        self.assertEqual(self.point == Point(1, (1,1)), False)
        
    def test_string(self):
        self.assertEqual(str(self.point), "0")
        self.point.set_state(1)
        self.assertEqual(str(self.point), ".")
        self.point.set_state(2)
        self.assertEqual(str(self.point), "X")
        self.point.set_state(3)
        self.assertEqual(str(self.point), "_")
        self.point.set_state(4)
        self.assertEqual(str(self.point), "0")
        self.point.set_state(100)
        self.assertNotEqual(str(self.point), "!")
        
def point_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPoint)

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship((0,0), 5, 0, [Point(0, (x, 0)) for x in range(5)])
        
    def test_get_points(self):
        self.assertEqual(self.ship.get_points(), [Point(0, (x,0)) for x in range(5)])
        
    def test_set_points(self):
        self.assertEqual(self.ship.set_points([Point(0, (x,0)) for x in range(5,10)]), True)
        self.assertEqual(self.ship.get_points(), [Point(0, (x,0)) for x in range(5,10)])
        
    def test_get_hits(self):
        self.assertEqual(self.ship.get_hits(), [0] * self.ship.get_size())
        
    def test_set_hits(self):
        self.assertEqual(self.ship.set_hits([1] * self.ship.get_size()), True)
        self.assertEqual(self.ship.get_hits(), [1] * self.ship.get_size())
        
    def test_get_orientation(self):
        self.assertEqual(self.ship.get_orientation(), 0)
        
    def test_set_orientation(self):
        self.assertEqual(self.ship.set_orientation(1), True)
        self.assertEqual(self.ship.get_orientation(), 1)
        
    def test_get_size(self):
        self.assertEqual(self.ship.get_size(), 5)
        
    def test_set_size(self):
        self.assertEqual(self.ship.set_size(2), True)
        self.assertEqual(self.ship.get_size(), 2)
        
    def test_get_start(self):
        self.assertEqual(self.ship.get_start(), (0,0))
                
    def test_set_start(self):
        self.assertEqual(self.ship.set_start((1,1)), True)
        self.assertEqual(self.ship.get_start(), (1,1))
        
    def test_is_hit(self):
        self.assertEqual(self.ship.is_hit(Point(0, (0,0))), True)
        self.assertEqual(self.ship.is_hit(Point(0, (100, 100))), False)
        
    def test_is_sunk(self):
        self.assertEqual(self.ship.is_sunk(), False)
        self.ship.set_hits([1] * self.ship.get_size())
        self.assertEqual(self.ship.is_sunk(), True)
        
    def test_string(self):
        self.assertEqual(str(self.ship), "[0 0 0 0 0 ]")
         
def ship_suite():    
    return unittest.TestLoader().loadTestsFromTestCase(TestShip)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player(self.board)
    
    def test_get_board(self):
        self.assertEqual(self.player.get_board(), self.board)
        
    def test_set_board(self):
        self.assertEqual(self.player.set_board(Board()), True)
        
    def test_is_hit(self):
        ship = self.board._ship2[0]
        self.assertEqual(self.player.is_hit(ship.get_points()[0]), True)
        
    def test_is_defeated(self):
        self.assertEqual(self.player.is_defeated(), False)
        
    def test_get_move(self):
        self.assertEqual(self.player.get_move(), (0,0))
        
    def test_get_ships_left(self):
        self.assertEqual(self.player.get_ships_left(), 5)
    
def player_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
    
class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(Board(), 0)
    
    def test_get_side(self):
        self.assertEqual(self.user.get_side(), 0)
        
    def test_set_side(self):
        self.assertEqual(self.user.set_side(1), True)
    
def user_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestUser)

class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI(Board(), 0)
    
    def test_get_difficulty(self):
        self.assertEqual(self.ai.get_difficulty(), 0)
        
    def test_set_difficulty(self):
        self.assertEqual(self.ai.set_difficulty(1), True)
        
def ai_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAI)

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_get_ships_left(self):
        self.assertEqual(self.board.get_ships_left(), 5)
        
    def test_get_size(self):
        self.assertEqual(self.board.get_size(), 10)
        
    def test_set_size(self):
        self.assertEqual(self.board.set_size(100), True)
        
    def test_is_hit(self):
        ship = self.board._ship2[0]
        self.assertEqual(self.board.is_hit(ship.get_points()[0]), True)
        
    def test_is_defeated(self):
        self.assertEqual(self.board.is_defeated(), False)
        
def board_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBoard)

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(point_suite())
    runner.run(ship_suite())
    runner.run(player_suite())
    runner.run(user_suite())
    runner.run(ai_suite())
    runner.run(board_suite())