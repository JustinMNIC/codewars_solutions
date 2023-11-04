"""
https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
"""


def solver(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                possible_solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for X in range(9):
                    if puzzle[r][X] in possible_solutions:
                        possible_solutions.remove(puzzle[r][X])
                    if puzzle[X][c] in possible_solutions:
                        possible_solutions.remove(puzzle[X][c])
                for R in range(3):
                    for C in range(3):
                        if r < 3:
                            if c < 3:
                                if puzzle[R][C] in possible_solutions:
                                    possible_solutions.remove(puzzle[R][C])
                            elif c < 6:
                                if puzzle[R][C + 3] in possible_solutions:
                                    possible_solutions.remove(puzzle[R][C + 3])
                            elif c < 9:
                                if puzzle[R][C + 6] in possible_solutions:
                                    possible_solutions.remove(puzzle[R][C + 6])
                        elif r < 6:
                            if c < 3:
                                if puzzle[R + 3][C] in possible_solutions:
                                    possible_solutions.remove(puzzle[R + 3][C])
                            elif c < 6:
                                if puzzle[R + 3][C + 3] in possible_solutions:
                                    possible_solutions.remove(puzzle[R + 3][C + 3])
                            elif c < 9:
                                if puzzle[R + 3][C + 6] in possible_solutions:
                                    possible_solutions.remove(puzzle[R + 3][C + 6])
                        elif r < 9:
                            if c < 3:
                                if puzzle[R + 6][C] in possible_solutions:
                                    possible_solutions.remove(puzzle[R + 6][C])
                            elif c < 6:
                                if puzzle[R + 6][C + 3] in possible_solutions:
                                    possible_solutions.remove(puzzle[R + 6][C + 3])
                            elif c < 9:
                                if puzzle[R + 6][C + 6] in possible_solutions:
                                    possible_solutions.remove(puzzle[R + 6][C + 6])
                if len(possible_solutions) == 1:
                    puzzle[r][c] = possible_solutions[0]

def checker(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return True
    return False

def sudoku(puzzle):
    while checker(puzzle):
        solver(puzzle)
    return puzzle







print(sudoku([[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]))



