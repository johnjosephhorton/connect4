#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pandas import DataFrame

empty =  "⚪"
black = "⚫"
red =  "🔴"

num_rows = 6
num_cols = 7
num_to_win = 4

# adds a position in a direction together like they were vectors
def Add(a,b): return [sum(x) for x in zip(a,b)] 

board = [[empty for i in range(num_cols)] for j in range(num_rows)]

def GetPiece(p):
    """Gets the piece at a board; returns None if we're out of range. 
       This function is just so we dont' have to check our index ranges each time. """
    row, column = p
    if row >= 0 and row < num_rows and column >= 0 and column < num_cols:
        return board[row][column]
    else:
        return None 

def AddPiece(column, color):
    """Figures out what row a dropped in piece will be at & updates the board. """
    spot = num_rows - 1
    for i in range(num_rows):
        if board[i][column] != empty:
            spot = i - 1
            break
    if spot < 0:
        print("Sorry - this column is full!")
        return None
    else:
        board[spot][column] = color
    return spot

def ChainLength(p, direction, color):
    """Gratuitous use of recursion because it is cool---figures out how long you can go in a direction"""
    if color == GetPiece(Add(p,direction)):
        return 1 + ChainLength(Add(p,direction), direction, color)
    else:
        return 0

def IsWinner(p, color):
    """Get the chain lengths in all the possible directions (except due north).
       We don't need to check north because we are only checking newly added pieces
       that were just dropped in. If the max chain length is long enough, declare a winner."""
    s =  ChainLength(p, (0,  -1), color)
    sw = ChainLength(p, (-1, -1), color)
    w =  ChainLength(p, (-1,  0), color)
    se = ChainLength(p, ( 1, -1), color)
    e  = ChainLength(p, ( 1,  0), color)
    ne = ChainLength(p, ( 1,  1), color)
    nw = ChainLength(p, (-1,  1), color)
    longest_chain = max([s, sw + ne, w + e, se + nw])
    if longest_chain >= num_to_win - 1:
        return True
    else:
        return False 
             
def PlayGame(): 
    print("Welcome!") 
    print("Black goes first")
    color = black
    while True:
        print(DataFrame(board))
        print("")
        column = int(raw_input("Player %s, select a column (0 to 6)?" % color))
        row = AddPiece(column, color) 
        if row is not None:
            if IsWinner((row, column), color):
                print("The winner is %s " % color)
                break
            color = black if color == red else red
    print("")
    print("")
    print("Final board:")
    print(DataFrame(board))

if __name__ == "__main__":
    PlayGame()
