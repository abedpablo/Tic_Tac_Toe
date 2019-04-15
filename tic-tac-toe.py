from tkinter import *
import os
import sys

root = Tk()
root.wm_title("Abed's Tic Tac Toe")

o_photo = PhotoImage(file = '/Users/abedpablo/Documents/o_image81.png')
x_photo = PhotoImage(file = '/Users/abedpablo/Documents/x_image81.png')
blue = PhotoImage(file = '/Users/abedpablo/Documents/blue81.gif')

turn = x_photo
mark: str = 'X'
combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #List format of possible winning combinations
board = [" "]*9 #board to hold Xs and Os for the winning function


def find_winner(b):
    for i in range(0, len(combinations)):
        combination = combinations[i]
        if(b[combination[0]] == b[combination[1]] and b[combination[1]] == b[combination[2]] and
            b[combination[0]] != " "):
                return b[combination[0]]
    return " "


def nextTurn():
    global turn
    turn = x_photo if turn == o_photo else o_photo
    global mark
    mark = 'X' if mark == 'O' else 'O'


def click(label, x, y):
    print('clicked', x, " ", y)
    label['image'] = turn
    board[x + 3*y] = mark
    winner = find_winner(board)
    if(winner != " "):
        w.configure(text = (mark + " has won the game!"))
    nextTurn()


def addLabel(parent, image, x, y):
    label = Label(parent, image = image, bg = 'blue')
    label.grid(row = y, column = x, padx= 7, pady = 7)
    label.bind("<Button-1>", lambda event : click(label, x, y))


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)


w = Label(root, text = 'May the best player win.')
C = Canvas(root, bg="blue", height=300, width=300)
line1 = C.create_line(100, 0, 100, 300, fill = "yellow", dash = (4, 4))
line2 = C.create_line(200, 0, 200, 300, fill = 'yellow', dash = (3, 3))
line3 = C.create_line(0, 100, 300, 100, fill = 'yellow')
line4 = C.create_line(0, 200, 300, 200, fill = 'yellow')
blabel = Label(root, bg = 'red', height=3, width = 20)
refresh = Button(blabel, text = 'Refresh', font = ('Helvetica', 10, 'italic'), height = 2, width = 9, command = restart)

for x in range(0, 3):
    for y in range(0, 3):
        addLabel(C, blue, x, y)

refresh.grid()
w.grid()
C.grid()
blabel.grid(sticky = S)

root.mainloop()
