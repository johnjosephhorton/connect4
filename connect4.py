#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import DataFrame

empty =  "⚪"
black = "⚫"
red =  "🔴"

num_rows = 6
num_cols = 7
num_to_win = 4

board = [[empty for i in range(num_cols)] for j in range(num_rows)]

def WinningPiece(row, column, color):
    return False 

#def Winner(board):
    


def AddPiece(column, color):
    spot = num_rows - 1
    for i in range(num_rows):
        if board[i][column] != empty:
            print(spot)
            spot = i - 1
            break
    if spot < 0:
        print("Sorry - this column is full!")
        return False
    else:
        board[spot][column] = color
    return True


print("Welcome!") 
print("Black goes first")
color = black
while True:
    print(DataFrame(board))
    print("")
    row = int(raw_input("Player %s, select a column (0 to 6)?" % color))
    if AddPiece(row, color):
        color = black if color == red else red

