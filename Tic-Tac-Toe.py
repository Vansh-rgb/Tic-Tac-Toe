import os
p1 = 'o'
p2 = 'x'
x1 = ' '
x2 = ' '
x3 = ' '
x4 = ' '
x5 = ' '
x6 = ' '
x7 = ' '
x8 = ' '
x9 = ' '

def wincheck(a=0):
    if a == 1:
        if (x1 == p1 and x2 == p1 and x3 == p1) or (x1 == p1 and x4 == p1 and x7 == p1) or (x1 == p1 and x5 == p1 and x9 == p1) or (x2 == p1 and x5 == p1 and x8 == p1) or (x3 == p1 and x6 == p1 and x9 == p1) or (x4 == p1 and x5 == p1 and x6 == p1) or (x7 == p1 and x8 == p1 and x9 == p1) or (x7 == p1 and x5 == p1 and x3 == p1):
            print("Player 1 wins!!!!")
            return 3
        else:
            return 0
    elif a == 2:
        if (x1 == p2 and x2 == p2 and x3 == p2) or (x1 == p2 and x4 == p2 and x7 == p2) or (x1 == p2 and x5 == p2 and x9 == p2) or (x2 == p2 and x5 == p2 and x8 == p2) or (x3 == p2 and x6 == p2 and x9 == p2) or (x4 == p2 and x5 == p2 and x6 == p2) or (x7 == p2 and x8 == p2 and x9 == p2) or (x7 == p2 and x5 == p2 and x3 == p2):
            print("Player 2 wins!!!!")
            return 4
        else:
            return 0

def board(p=0,inp=0):
    global x1
    global x2
    global x3
    global x4
    global x5
    global x6
    global x7
    global x8
    global x9

    if p == 1 and inp == 1:
        x1 = p1
    elif p == 1 and inp == 2:
        x2 = p1
    elif p == 1 and inp == 3:
        x3 = p1
    elif p == 1 and inp == 4:
        x4 = p1
    elif p == 1 and inp == 5:
        x5 = p1
    elif p == 1 and inp == 6:
        x6 = p1
    elif p == 1 and inp == 7:
        x7 = p1
    elif p == 1 and inp == 8:
        x8 = p1
    elif p == 1 and inp == 9:
        x9 = p1
    elif p == 2 and inp == 1:
        x1 = p2
    elif p == 2 and inp == 2:
        x2 = p2
    elif p == 2 and inp == 3:
        x3 = p2
    elif p == 2 and inp == 4:
        x4 = p2
    elif p == 2 and inp == 5:
        x5 = p2
    elif p == 2 and inp == 6:
        x6 = p2
    elif p == 2 and inp == 7:
        x7 = p2
    elif p == 2 and inp == 8:
        x8 = p2
    elif p == 2 and inp == 9:
        x9 = p2
    os.system("cls")
    print(f'             |              |              \n             |              |              \n      {x7}      |      {x8}       |      {x9}       \n             |              |              \n             |              |              \n-----------------------------------------\n             |              |              \n             |              |              \n      {x4}      |      {x5}       |      {x6}       \n             |              |              \n             |              |              \n-----------------------------------------\n             |              |              \n             |              |              \n      {x1}      |      {x2}       |      {x3}       \n             |              |              \n             |              |              ')


def play():
    turn = 0
    gamelist = []
    board()
    while(turn <= 9):
        
        while(turn%2 == 0):
            t = int(input("Player 1, Enter your place(1-9):\n      7             8             9\n\n\n      4             5             6\n\n\n      1             2             3\n->"))
            if t in gamelist:
                os.system("cls")
                board()
                print("Wrong choice, Enter again")
            else:
                os.system("cls")
                gamelist.append(t)
                board(1,t)
                y = wincheck(1)
                if y == 3:
                    turn = 9
                    break
                turn+=1
        if turn == 9:
            break
        while(turn%2 == 1):
            t = int(input("Player 2, Enter your place(1-9):\n      7             8             9\n\n\n      4             5             6\n\n\n      1             2             3\n->"))
            if t in gamelist:
                os.system("cls")
                board()
                print("Wrong choice, Enter again")
            else:
                os.system("cls")
                gamelist.append(t)
                board(2,t)
                z = wincheck(2)
                if z == 4:
                    turn = 9
                    break
                turn+=1
        if turn == 9:
            break
    print("ENDGAME")

def welcome():
    c = 'YES'
    while(c == 'YES'):
        nw = 0
        flag = 0
        os.system("cls")
        global p1
        global p2
        print("Welcome to Tic Tac Toe\nRules:See your numpad and the postion on the board will be as follows:\n7  8  9\n4  5  6\n1  2  3\n")
        p1 = input("Hey Player 1, choose X or O\nEnter Here:")
        p1 = p1.upper()
        if p1 == 'X':
            p2 = 'O'
            c = 'no'
        elif p1 == 'O':
            p2 = 'X'
            c = 'no'
        else:
            flag+=1
            os.system("cls")
            c = input("Wrong choice\nDo you want to continue?(type 'yes' to continue/press any key to exit):")
            c = c.upper()
            if (c != 'YES'):
                nw = 1
                break
        if nw == 1:
            break
    if flag == 0:
        print(f'Player 1 => {p1} and Player 2 => {p2}')
    f = 0
    while(f == 0 and nw == 0):
        g = input("Type 'GO':")
        g = g.upper()
        if g == 'GO':
            f = 1
            play()
        else:
            os.system("cls")
            print('Wrong choice!!!!!!!')
welcome()
