from ai import AI
from user import User
from board import Board
from point import Point
import pygame
import time
from PIL import Image, ImageDraw

class Game:
    def __init__(self):
        # get user input for board size and number of ships, if input is invalid it gets re-asked
        while True:
            try:
                size = raw_input("Please enter a size for the board [10]: ")
                if size == "":
                    size = 10
                else:
                    size = int(size)
                    if size < 1:
                        raise ValueError
                break
            except ValueError:
                continue
        while True:
            try:
                ships2 = raw_input("Please enter the amount of size 2 ships [1]: ")
                if ships2 == "":
                    ships2 = 1
                else:
                    ships2 = int(ships2)
                    if ships2 < 0:
                        raise ValueError
                    # preliminary check for whether the ships will fit on the board
                    # if the total area of ships is greater than the area of the board
                    # than there is no chance of the ships fitting and a new value is asked for
                    # this check is done for all ships and does not take into account previously
                    # added ships
                    if ships2 > size * size / 2:
                        print "The ships will not fit on the board"
                        raise ValueError
                break
            except ValueError:
                continue
        while True:
            try:
                ships3 = raw_input("Please enter the amount of size 3 ships [2]: ")
                if ships3 == "":
                    ships3 = 2
                else:
                    ships3 = int(ships3)
                    if ships3 < 0:
                        raise ValueError
                    if ships3 > size * size / 3:
                        print "The ships will not fit on the board"
                        raise ValueError
                break
            except ValueError:
                continue
        while True:
            try:
                ships4 = raw_input("Please enter the amount of size 4 ships [1]: ")
                if ships4 == "":
                    ships4 = 1
                else:
                    ships4 = int(ships4)
                    if ships4 < 0:
                        raise ValueError
                    if ships4 > size * size / 4:
                        print "The ships will not fit on the board"
                        raise ValueError
                break
            except ValueError:
                continue
        while True:
            try:
                ships5 = raw_input("Please enter the amount of size 5 ships [1]: ")
                if ships5 == "":
                    ships5 = 1
                else:
                    ships5 = int(ships5)
                    if ships5 < 0:
                        raise ValueError
                    if ships5 > size * size / 5:
                        print "The ships will not fit on the board"
                        raise ValueError
                break
            except ValueError:
                continue
        # get user input for type of game
        if enhancements:
            while True:
                try:
                    game_type = raw_input("Please enter game type:\n\t0:Human vs. Human\n\t1:Human vs. Computer\n\t2:Computer vs. Computer\n[1]:\n")
                    if game_type == "":
                        game_type = 1
                    else:
                        game_type = int(game_type)
                        if game_type < 0 or game_type > 2:
                            raise ValueError
                    break
                except ValueError:
                    continue
        else:
            while True:
                try:
                    game_type = raw_input("Please enter game type:\n\t0:Human vs. Human\n\t1:Human vs. Computer\n[1]:\n")
                    if game_type == "":
                        game_type = 1
                    else:
                        game_type = int(game_type)
                        if game_type < 0 or game_type > 1:
                            raise ValueError
                    break
                except ValueError:
                    continue
        # create the players, their boards and ships, also ask for AI difficulty if enhancements are enabled
        # and a user is AI
        if game_type == 0:
            self._player1 = User(Board(size, ships2, ships3, ships4, ships5), 0)
            self._player2 = User(Board(size, ships2, ships3, ships4, ships5), 1)
        elif game_type == 1:
            difficulty = 0
            if enhancements:
                while True:
                    try:
                        difficulty = raw_input("Please enter a computer difficulty:\n\t0:Easy\n\t1:Hard\n[0]:\n")
                        if difficulty == "":
                            difficulty = 0
                        else:
                            difficulty = int(difficulty)
                            if difficulty < 0 or difficulty > 1:
                                raise ValueError
                        break
                    except ValueError:
                        continue
            self._player1 = User(Board(size, ships2, ships3, ships4, ships5), 0)
            self._player2 = AI(Board(size, ships2, ships3, ships4, ships5), difficulty)
        elif game_type == 2:
            difficulty = 0
            if enhancements:
                while True:
                    try:
                        difficulty = raw_input("Please enter a computer difficulty:\n\t0:Easy\n\t1:Hard\n[0]:\n")
                        if difficulty == "":
                            difficulty = 0
                        else:
                            difficulty = int(difficulty)
                            if difficulty < 0 or difficulty > 1:
                                raise ValueError
                        break
                    except ValueError:
                        continue
            self._player1 = AI(Board(size, ships2, ships3, ships4, ships5), difficulty)
            difficulty = 0
            if enhancements:
                while True:
                    try:
                        difficulty = raw_input("Please enter a computer difficulty:\n\t0:Easy\n\t1:Hard\n[0]:\n")
                        if difficulty == "":
                            difficulty = 0
                        else:
                            difficulty = int(difficulty)
                            if difficulty < 0 or difficulty > 1:
                                raise ValueError
                        break
                    except ValueError:
                        continue
            self._player2 = AI(Board(size, ships2, ships3, ships4, ships5), difficulty)
        else:
            print "Game type was incorrent"
            
        # if enhancements are enabled initialize and setup variables for the GUI display
        if enhancements:
            pygame.init()
            self._screen1 = pygame.display.set_mode(((size * 22) + 1,(size * 11) + 50))
            self._screen1.fill((0,0,0))
            self._font = pygame.font.Font(None, 30)
            self._ship_font = pygame.font.Font(None, 20)
        
    def start(self):
        # continue playing the game as long as someone has not lost
        turn_count = 0
        draw_ships = False
        while(not self._player1.is_defeated() and not self._player2.is_defeated()):
            # if enhancements are enabled generate the images to display for the GUI and display them
            if enhancements:
                for event in pygame.event.get(pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                self._screen1.fill((0,0,0))
                image, imagerect = self._player1.get_board().draw_board(draw_ships)
                imagerect.top += 50
                image1, imagerect1 = self._player2.get_board().draw_board(draw_ships)
                imagerect1.top += 50
                imagerect1.left = imagerect.width + 1
                self._screen1.blit(image, imagerect)
                self._screen1.blit(image1, imagerect1)
                # create the 'scoreboard' for the GUI with the player name highlighted for
                # whoever's turn it currently is
                if turn_count % 2 == 0:
                    self._font.set_bold(True)
                else:
                    self._font.set_bold(False)
                font_image = self._font.render("Player 1", False, (255,255,255))
                self._screen1.blit(font_image, pygame.Rect(0,0,self._font.size("Player 1")[0], self._font.size("Player 1")[1]))
                ship_image = self._ship_font.render("ships left = " + str(self._player1.get_ships_left()), False, (255,255,255))
                self._screen1.blit(ship_image, pygame.Rect(0,30,self._ship_font.size("ships left = " + str(self._player1.get_ships_left()))[0], self._ship_font.size("ships left = " + str(self._player1.get_ships_left()))[1]))
                if turn_count % 2 != 0:
                    self._font.set_bold(True)
                else:
                    self._font.set_bold(False)
                font_image = self._font.render("Player 2", False, (255,255,255))
                self._screen1.blit(font_image, pygame.Rect(self._screen1.get_width() - self._font.size("Player 2")[0],0,self._font.size("Player 2")[0], self._font.size("Player 2")[1]))
                ship_image = self._ship_font.render("ships left = " + str(self._player2.get_ships_left()), False, (255,255,255))
                self._screen1.blit(ship_image, pygame.Rect(self._screen1.get_width() - self._ship_font.size("ships left = " + str(self._player2.get_ships_left()))[0],30,self._ship_font.size("ships left = " + str(self._player2.get_ships_left()))[0], self._ship_font.size("ships left = " + str(self._player2.get_ships_left()))[1]))
                pygame.display.update()
            # get player 1 or player 2 move and check for hit and update board
            if turn_count % 2 == 0:
                if not enhancements:
                    print self._player1.get_board()
                value = self._player2.is_hit(Point(0, self._player1.get_move()))
                if value:
                    self._player1.set_prev_was_hit(True)
                elif self._player1.get_prev_was_hit() and not value:
                    self._player1.next_direction()
            else:
                if not enhancements:
                    print self._player2.get_board()
                value = self._player1.is_hit(Point(0, self._player2.get_move()))
                if value:
                    self._player2.set_prev_was_hit(True)
                elif self._player2.get_prev_was_hit() and not value:
                    self._player2.next_direction()
            # change players turn
            turn_count += 1
        # if enhancements are enabled display the final display after a player has won
        if enhancements:
            self._screen1.fill((0,0,0))
            self._font.set_bold(False)
            font_image = self._font.render("Player 1", False, (255,255,255))
            self._screen1.blit(font_image, pygame.Rect(0,0,self._font.size("Player 1")[0], self._font.size("Player 1")[1]))
            font_image = self._font.render("Player 2", False, (255,255,255))
            self._screen1.blit(font_image, pygame.Rect(self._screen1.get_width() - self._font.size("Player 2")[0],0,self._font.size("Player 2")[0], self._font.size("Player 2")[1]))
        # display who was the winner of the game
        if self._player1.is_defeated():
            if not enhancements:
                print "Player 2 Wins."
                print self._player1.get_board()
            else:
                end_image = self._ship_font.render("Player 2 Wins.", False, (255,255,255))
                self._screen1.blit(end_image, pygame.Rect(0,30, self._ship_font.size("Player 2 Wins.")[0], self._ship_font.size("Player 2 Wins.")[1]))
        elif self._player2.is_defeated():
            if not enhancements:
                print "Player 1 Wins."
                print self._player2.get_board()
            else:
                end_image = self._ship_font.render("Player 1 Wins.", False, (255,255,255))
                self._screen1.blit(end_image, pygame.Rect(0,30, self._ship_font.size("Player 1 Wins.")[0], self._ship_font.size("Player 1 Wins.")[1]))
        # if enhancements are enabled display the actual boards of the players after one has won
        if enhancements:
            image, imagerect = self._player1.get_board().draw_board(draw_ships)
            imagerect.top += 50
            image1, imagerect1 = self._player2.get_board().draw_board(draw_ships)
            imagerect1.top += 50
            imagerect1.left = imagerect.width + 1
            self._screen1.blit(image, imagerect)
            self._screen1.blit(image1, imagerect1)        
            pygame.display.update()
            # wait for a mouse click to allow the users to see the outcome of the game
            while len(pygame.event.get(pygame.MOUSEBUTTONUP)) == 0:
                continue
