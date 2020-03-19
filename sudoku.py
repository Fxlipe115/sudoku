#!/usr/bin/python3
import curses
import numpy as np
import argparse
import re

from sudokusolver import Sudoku

class SudokuController:
    
    def __init__(self, game, scr):
        #self.scr = curses.newwin(30, 50)
        self.scr = scr
        self.game = game
        self.cursor_x = 0
        self.cursor_y = 0
        self.screen_coord = [
                                [(y,x) for x in range(2,38,4)] 
                                    for y in range(1,26,2)
                            ]
        self.editable = [
                            [self.game.board[y, x] == 0 
                                for x in range(9)]
                                for y in range(9)
                        ]
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        self.BLACK = curses.color_pair(1)
        self.RED = curses.color_pair(2)
        self.GREEN = curses.color_pair(3)
        self.YELLOW = curses.color_pair(4)

    def play(self):
        self.scr.clear()

        self.print_board()
        self.print_numbers()

        pressed_key = -1
        while True:

            if pressed_key == -1:
                pass
            elif pressed_key == curses.KEY_LEFT:
                self.cursor_x -= 1
            elif pressed_key == curses.KEY_DOWN:
                self.cursor_y += 1
            elif pressed_key == curses.KEY_RIGHT:
                self.cursor_x += 1
            elif pressed_key == curses.KEY_UP:
                self.cursor_y -= 1
            elif (chr(pressed_key).isdecimal() and 
                    self.editable[self.cursor_y][self.cursor_x]):
                if chr(pressed_key) == '0':
                    self.game.board[self.cursor_y, self.cursor_x] = 0
                else:
                    self.game.board[self.cursor_y, 
                            self.cursor_x] = int(chr(pressed_key))
                
            self.print_numbers()
            self.scr.move(*self.screen_coord[self.cursor_y][self.cursor_x])
            self.scr.refresh()

            pressed_key = self.scr.getch()


    def print_numbers(self):
        for y,line in enumerate(self.game.board):
            for x,number in enumerate(line):
                cell_value = str(number) if number != 0 else ' '
                attr = self.BLACK
                if self.editable[y][x]: 
                    if self.game.possible(y, x, number):
                        attr = self.GREEN
                    else:
                        attr = self.RED
                #if number == self.game.board[self.cursor_y, 
                #                             self.cursor_x]:
                #    attr = self.YELLOW

                self.scr.addstr(*self.screen_coord[y][x], 
                        cell_value, attr)
                    
        
    def print_board(self):
        self.scr.addstr(0, 0, ('╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n'
                               '║   │   │   ║   │   │   ║   │   │   ║\n'
                               '╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝'
                              ), self.BLACK
                       )


def main(stdscr, game):
    control = SudokuController(game, stdscr)
    control.play()
    

if __name__ == '__main__':
    def game_input_type(arg_value):
        if not re.compile('^[0-9]{81}$').match(arg_value): 
            raise argparse.ArgumentTypeError(
                    'input must be in the format [0-9]{81}')
        return arg_value

    parser = argparse.ArgumentParser(description=
            'Process some integers.')
    parser.add_argument('game', type=game_input_type,
            help=('a string of numbers representing ' 
                  'the initial state of the board'))

    args = parser.parse_args()   
    input_string = args.game

    initial_numbers = [*map(int, input_string)]
    board_array = np.array(initial_numbers)
    board = board_array.reshape(9,9)

    game = Sudoku(board)
    curses.wrapper(main, game)

