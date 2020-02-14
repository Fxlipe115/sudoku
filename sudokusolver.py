#!/usr/bin/python3

import numpy as np
class Sudoku:
    def __init__(self, matrix):
        self.board = np.array(matrix)
        if self.board.shape != (9, 9):
            raise('Invalid format: Input must be a 9x9 matrix')

    def possible(self, y, x, n):
        for i in range(9):
            if self.board[y, i] == n:
                return False
        for i in range(9):
            if self.board[i, x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[y0+i, x0+j] == n:
                    return False
        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.board[y, x] == 0:
                    for n in range(1,10):
                        if self.possible(y,x,n):
                            self.board[y, x] = n
                            self.solve()
                            self.board[y, x] = 0
                    return
        print(self)
        
    def __str__(self):
        s = ('╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n'
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
             '╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝'
            )
        return s.format(*[' ' if x == 0 else x for x in self.board.flatten()])


if __name__ == '__main__':
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
    print('Solution:')
    game.solve()
