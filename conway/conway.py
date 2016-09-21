"""
http://coderetreat.org/gol
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
https://sites.google.com/site/tddproblems/all-problems-1/game-of-life
Game of life is a so called cellular automaton. You can read up all about it at wikipedia.

Develop an algorithm that takes "one step" in the game of life. The behaviour examples may simply be the rules of the
game:

   1. Any live cell with fewer than two live neighbours dies,
   as if caused by underpopulation.
   2. Any live cell with more than three live neighbours dies,
   as if by overcrowding.
   3. Any live cell with two or three live neighbours lives on
   to the next generation.
   4. Any dead cell with exactly three live neighbours becomes a live cell.

You also have to think of things such as how to represent the board in a test-friendly way,
and what "value" cells outside the board has. Or maybe the board does not have borders?
"""
import os
import random
import time


def build_board(x, y):
    lines, columns, board = clean(x), clean(y), list()
    if lines and columns:
        board = {(line, column) : dead_or_alive() for line in range(lines) for column in range(columns)}
    return lines, columns, board


def clean(val):
    if isinstance(val, str) and val.isdigit():
        return int(val)
    elif isinstance(val, int) and val > 0:
        return val
    else:
        return None


def dead_or_alive():
    return random.choice(['-', '-', '-', '-', '-', '-', '-', '+'])


def draw(board_info):
    lines, columns, board = board_info
    draw = list()
    for i in range(lines):
        for j in range(columns):
            draw.append(board[(i,j)])
        draw.append('\n')
    output = ''.join(draw)
    return output


def game_of_life(board_info):
    lines, columns, board = board_info
    for cell in board:
        neighbours_cell = neighbours(*cell, board_info)
        neighbours_alive = sum(1 for cell in neighbours_cell if is_alive(*cell, board))
        if is_alive(*cell, board) and neighbours_alive < 2:
            board[cell] = '-'
        elif is_alive(*cell, board) and neighbours_alive > 3:
            board[cell] = '-'
        elif is_alive(*cell, board) and neighbours_alive in (2, 3):
            board[cell] = '+'
        elif is_alive(*cell, board) == False and neighbours_alive == 3:
            board[cell] = '+'
    return lines, columns, board


def is_alive(x, y, board):
    return board[(x,y)] == '+'


def neighbours(x, y, board_info):
    neighbours = list()
    if x < board_info[0] and y < board_info[1]:
        xs = [xn for xn in [x-1, x, x+1] if xn >= 0]
        ys = [yn for yn in [y-1, y, y+1] if yn >= 0]
        neighbours = [(xn,yn)
            for xn in xs
            for yn in ys
            if (x,y) != (xn,yn) and xn < board_info[0] and yn < board_info[1]
        ]
    return neighbours


assert isinstance(build_board(8, 8), tuple)
assert isinstance(build_board(4, 4), tuple)
assert isinstance(build_board(0, 0), tuple)

assert build_board(-1, -1) == (None, None, [])
assert build_board(-5, -5) == (None, None, [])
assert build_board(-10, -10) == (None, None, [])

assert build_board(2, -2) == (2, None, [])
assert build_board(4, -4) == (4, None, [])
assert build_board(1000, -1000) == (1000, None, [])

assert build_board(-50, 50) == (None, 50, [])
assert build_board(-22, 22) == (None, 22, [])
assert build_board(-11, 11) == (None, 11, [])

assert build_board(-11, None) == (None, None, [])
assert build_board(None, None) == (None, None, [])
assert build_board(None, 33) == (None, 33, [])

assert build_board('x', 'z') == (None, None, [])
assert build_board(2, 'z') == (2, None, [])
assert build_board(4, '?') == (4, None, [])

assert len(build_board(3, 3)[2]) == 9
assert len(build_board(4, 4)[2]) == 16
assert len(build_board(4, 2)[2]) == 8
assert len(build_board(2, 4)[2]) == 8

assert draw(build_board(2, 2)).count('\n') == 2
assert draw(build_board(1, 1)).count('\n') == 1
assert draw(build_board(4, 4)).count('\n') == 4

assert dead_or_alive() in ['-', '+']
assert build_board('1', '1')[2] == '-' or '+'

assert neighbours(0, 0, build_board(4, 4)) == [(0, 1), (1,0), (1,1)]
assert neighbours(1, 1, build_board(4, 4)) == [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]
assert neighbours(3, 4, build_board(8, 8)) == [(2,3), (2,4), (2,5), (3,3), (3,5), (4,3), (4,4), (4,5)]

assert neighbours(1, 3, build_board(2, 8)) == [(0,2), (0,3), (0,4), (1,2), (1,4)]
assert neighbours(7, 1, build_board(8, 2)) == [(6,0), (6,1), (7,0)]
assert neighbours(7, 7, build_board(8, 8)) == [(6,6), (6,7), (7,6)]

assert neighbours(8, 8, build_board(8, 8)) == []
assert neighbours(2, 9, build_board(7, 7)) == []
assert neighbours(-2, 4, build_board(5, 8)) == []

assert isinstance(game_of_life(build_board(8, 8)), tuple)


board = build_board(64, 64)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(draw(game_of_life(board)),end='\r')
    time.sleep(1)
