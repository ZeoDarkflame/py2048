from GBoard import GameBoard #import the gameboard class, the heart of the code
import os
import time
try:
    from getch import getch      #import getch to hold the screen
except:
    print("getch not available, installing...")
    print("reopen the program after installation is complete")
    print("try installing pip3 if pip3 is not available")
    os.system("pip3 install getch; python3 -m pip install getch")     #install getch for the user
    time.sleep(5)
    exit()
from sys import argv         #to take arguments
from getopt import getopt    #to parse arguments

def check_power(n):          #to check whether the winning number entered is a power of 2 or not
    var = 2
    while(var <= n):
        if(n == var):
            return True
        var = var*2
    return False

#taking initial inputs
warning = "You cannot do that"
board_size = 5
cap_number = 2048
try:
    opts,args = getopt(argv[1:],'n:w:',['n=','w='])
except:
    print("USING DEFAULTS\n")
for opt,arg in opts:
    if opt == '-n' or opt == '--n':
        try:
            board_size = int(arg)
            if board_size < 1:
                print("board size not possible, using default")
                board_size = 5
        except:
            print("Using default board size")
            board_size = 5
    elif opt == '-w' or opt == '--w':
        try:
            cap_number = int(arg)
            if check_power(cap_number) == False:
                print("winning number not possible, using default")
                cap_number = 2048
        except:
            print("Using default winning number")
            cap_number = 2048
print("INTSTRUCTIONS\nWSAD are usual controls\nPress z to quit")
print("Press any key to continue...")


#intializing game
main_board = GameBoard(board_size,cap_number)
main_board.fillrandom()
warn = False
getch()

#Entering Main Game Loop
while(True):
    movemade = True
    main_board.print_board()
    print(main_board.win_number)
    if warn:
        print(warning)
        print("Make a different move")
    else:
        print("Make a move....")
    if board_size == 1:
        if(main_board.wincheck()):                  #We double check the winning before and after making the move to ensure the edge case works
            main_board.print_board()
            print("Congratulations you won")
            print("Press any key to continue...")
            getch()
            break
        if(not main_board.ispossible()):
            main_board.print_board()
            print("You Lost")
            print("Press any key to continue...")
            getch()
            break
    move = getch()
    if(move == 'a'):
        if(main_board.left()):
            main_board.states.append(main_board.board)      #added undo stack
            main_board.board = main_board.moveleft(main_board.board)
            warn = False
        else:
            warn = True
            continue
    elif(move == 'd'):
        if(main_board.right()):
            main_board.states.append(main_board.board) 
            main_board.board = main_board.moveright(main_board.board)
            warn = False
        else:
            warn = True
            continue
    elif(move == 'w'):
        if(main_board.up()):
            main_board.states.append(main_board.board) 
            main_board.board = main_board.moveup(main_board.board)
            warn = False
        else:
            warn = True
            continue
    elif(move == 's'):
        if(main_board.down()):
            main_board.states.append(main_board.board) 
            main_board.board = main_board.movedown(main_board.board)
            warn = False
        else:
            warn = True
            continue
    elif(move == 'z'):
        exit()
    elif(move == 'u'):             #implementing undo stack
        if len(main_board.states) != 0:
            main_board.board = main_board.states.pop()
            movemade = False
        else:
            print("You cannot undo...press any key to continue")
            movemade = False
            getch()
    else:
        movemade = False
    if movemade == True:
        if(main_board.wincheck()):                  #We double check the winning before and after making the move to ensure the edge case works
            main_board.print_board()
            print("Congratulations you won")
            print("Pess any key to continue...")
            getch()
            break
        main_board.fillrandom()
        if not any(row.count(0) != 0 for row in main_board.board):  #this makes the game a bit faster
            if(not main_board.ispossible()):
                main_board.print_board()
                print("You Lost")
                print("Press any key to continue...")
                getch()
                break
    
