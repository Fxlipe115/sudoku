import curses
import numpy as np

from sudokucontroller import SudokuController
from sudokusolver import Sudoku

def main(stdscr):
    input_string = input()

    try:
        initial_numbers = [*map(int, input_string)]
        board_array = np.array(initial_numbers)
        board = board_array.reshape(9,9)
    except ValueError:
        raise SystemExit('Invalid input format: ' \
                         'input must be in the format [0-9]{81}')

    game = Sudoku(board)
    print('Original:')
    print(game)

    #stdscr.clear()
    curses.echo
    cont = SudokuController(stdscr, game)
    cont.play()
    
curses.wrapper(main)

