import curses
import numpy as np

from sudokusolver import Sudoku

class SudokuController:
    
    def __init__(self, scr, game):
        self.scr = scr
        self.game = game
        self.cursor_x = 0
        self.cursor_y = 0

    def play(self):
        self.scr.clear()
        while True:
            try:
                pressed_key = self.scr.getkey()
            except Exception:
                pass
            else:
                if pressed_key.isdigit():
                    self.game.board[0,0] = int(pressed_key)
                    break

            self.print_board()

            self.scr.refresh()
        
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
