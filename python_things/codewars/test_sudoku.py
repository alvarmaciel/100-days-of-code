import pytest
from python_things.codewars.sudoku import check_row

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def column(matrix, i):
    return [row[i] for row in matrix]



def test_check_row():
    # given
    value_to_check = 3
    # when
    row_to_check = puzzle[0]
    # then
    assert check_row(value_to_check, row_to_check) == False

def test_check_column():
    # given
    value_to_check = 8
    # when
    column_to_check = column(puzzle, 3)
    # then
    assert check_column(value_to_check, column_to_check) == False