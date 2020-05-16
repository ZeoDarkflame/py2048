import os                       #import os to apply cls on windows terminal
import random                   #import random to generate random number using randrange()
from copy import deepcopy       #import deepcopy for copying lists

#this function is used to power all moves
def lsa(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j] != 0 and a[j] != a[i]:
                break
            if a[j] != 0 and a[j] == a[i]:
                a[i] = a[i] + a[j]
                a[j] = 0
                break
    for i in range(len(a)):
        if a[i] == 0:
            for j in range(i+1,len(a)):
                if a[j] != 0:
                    a[i] = a[j]
                    a[j] = 0
                    break
    return a

#board class of game
class GameBoard():
    def __init__(self,size,winning_number):
        self.size = size
        self.win_number = winning_number
        self.empty = self.size*self.size
        self.board = []
        self.states = []
        self.create_board()

    def printno(self,n):        #this function is used to print the game board with uniform spaces
        if n < 10:
            print(n,end="    ")
        elif n < 100:
            print(n,end="   ")
        elif n < 1000:
            print(n,end="  ")
        elif n < 10000:
            print(n,end=" ")

    def create_board(self):     #this function initalizes the game board
        temp_list = []
        for i in range(self.size):
            for j in range(self.size):
                temp_list.append(0)
            self.board.append(temp_list[:])
            temp_list.clear()
    
    def print_board(self):      #this function uses the printno to print the board
        os.system('cls')
        for row in self.board:
            for i in row:
                self.printno(i)
            print("\n")

    def wincheck(self):         #this function checks for victory
        emptycells = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    emptycells += 1
                if self.board[i][j] == self.win_number:
                    return True
        self.empty = emptycells
        return False
        
    def fillrandom(self):       #this function is used to fill random empty space with 2
        num = random.randrange(0,self.empty)
        emptycells = 0
        done = False
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    if emptycells == num:
                        self.board[i][j] = 2
                        done = True
                        break
                    else:
                        emptycells += 1
            if done:
                break
        #self.empty -= 1
        return num

    #functions to make moves
    def moveleft(self,board):
        aux_board = deepcopy(board)
        for row in aux_board:
            lsa(row)
        return aux_board

    def moveright(self,board):
        aux_board = deepcopy(board)
        for row in aux_board:
            row.reverse()
            lsa(row)
            row.reverse()
        return aux_board

    def rotateboard(self,board):        #this function powers the moveup and movedown functions
        rotated_board = []
        tlist = []
        for i in range(self.size):
            for j in range(self.size):
                tlist.append(board[j][i])
            rotated_board.append(tlist[:])
            tlist.clear()
        rotated_board.reverse()
        return rotated_board

    def moveup(self,board):
        aux_board = self.rotateboard(deepcopy(board))
        aux_board = self.moveleft(aux_board)
        #instead of creating a rotateboard CW function, we use the rotateboard function thrice to achieve the same effect
        aux_board = self.rotateboard(aux_board[:])
        aux_board = self.rotateboard(aux_board[:])
        aux_board = self.rotateboard(aux_board[:])
        return aux_board

    def movedown(self,board):
        aux_board = self.rotateboard(deepcopy(board))
        aux_board = self.moveright(aux_board)
        #instead of creating a rotateboard CW function, we use the rotateboard function thrice to achieve the same effect
        aux_board = self.rotateboard(aux_board[:])
        aux_board = self.rotateboard(aux_board[:])
        aux_board = self.rotateboard(aux_board[:])
        return aux_board

    #functions to check whether it is possible to make certain moves
    def left(self):
        if self.board == self.moveleft(self.board):
            return False
        else:
            return True

    def right(self):
        if self.board == self.moveright(self.board):
            return False
        else:
            return True

    def up(self):
        if self.board == self.moveup(self.board):
            return False
        else:
            return True

    def down(self):
        if self.board == self.movedown(self.board):
            return False
        else:
            return True

    def ispossible(self):       #this function checks whether making a move is possible
        if self.down() or self.up() or self.left() or self.right():
            return True
        else:
            return False

if __name__ == "__main__":
    print("Open the MainLine.py file")