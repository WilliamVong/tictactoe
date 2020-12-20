"""
Tic Tac Toe Player
"""
import sys
import math
from collections import Iterable
import copy
import numpy as np


X = "X"
O = "O"
EMPTY = None


testingboard = [[EMPTY, O, X], [X, O, EMPTY], [EMPTY, EMPTY, EMPTY]]
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def conversion(board):
    return [tuple(l) for l in board]

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def flatten(board):
     for item in board:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:
             yield item

def unflatten(board):
    i=0
    new_list=[]
    while i<len(data_list):
            new_list.append(data_list[i:i+3])
            i+=3
    return new_list

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counterX = 0
    counterO = 0
    seen = set()
    flatboard = flatten(board)
    for elm in flatboard:
        if 'X' in flatboard:
            counterX += 1
            seen.add(elm)
        elif 'O' in flatboard:
            counterO += 1
            seen.add(elm)
        else:
            seen.add(elm)
    if counterO == counterX:
        return X
    elif counterX > counterO:
        return O
    else:
        raise Exception("Illegal Game Board")

    actions(testingboard)

# -> O's turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    flatboard = flatten(board)
    setactions = list_duplicates_of(flatboard, EMPTY)
    #yes, it's not efficient, sorry
    replacedict = {1:(1, 1), 2:(2, 1), 3:(3, 1), 4:(1, 2), 5:(2, 2), 6:(3, 2),7:(1, 3), 8:(2, 3), 9:(3, 3)}

    res = [replacedict.get(n, n) for n in setactions]

    return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except IndexError:
        print('Spot already occupied')



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #transposition to check rows, then columns
    for Board1 in [board, np.transpose(board)]:
        result = checkRows(Board1)
        if result:
            return result
    return checkDiagonals(board)




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
        # Checks if board is full or if there is a winner
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
