import curses
import numpy as np

from sudokusolver import Sudoku

class SudokuController:
    
    def __init__(self, game):
        self.scr = curses.newwin(19, 38)
        self.game = game
        self.cursor_x = 0
        self.cursor_y = 0
        self.screen_coord = [
                                [(y,x) for x in range(2,38,4)] 
                                    for y in range(1,9,3)
                            ]

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


def main(stdscr):
    input_string = input()

    try:
        initial_numbers = [*map(int, input_string)]
        board_array = np.array(initial_numbers)
        board = board_array.reshape(9,9)
    except ValueError:
        raise SystemExit('Invalid input format: ' \
                         'input must be in the format [0-9]{81}')

    curses.echo()
    #curses.curs_set(0)

    game = Sudoku(board)

    control = SudokuController(game)
    control.play()
    

if __name__ == '__main__':
    curses.wrapper(main)

