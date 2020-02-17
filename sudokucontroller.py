import numpy as np
import curses

from sudokusolver import Sudoku

class SudokuController:
    
    def __init__(self, scr, game):
        self.scr = scr
        self.game = game
        self.cursor_x = 0
        self.cursor_y = 0

        #self.scr.nodelay(True)

    def play(self):
        self.scr.clear()
        self.print_board()
        self.scr.refresh()

        pressed_key = -1
        curses.nocbreak()

        while True:
            if pressed_key != -1:
                self.game.board[0,0] = int(pressed_key)
                self.scr.addstr(0, 0, str(pressed_key))

            
            #self.scr.addstr(1,2,'A')

            self.scr.refresh()

            pressed_key = self.scr.getch()
        
    def print_board(self):
        self.scr.addstr(0, 0, ('╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n'
                               '╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝'.format(
                                        *[' ' if x == 0 else x 
                                            for x in self.game.board.flatten()]
                                   )
                              ))
