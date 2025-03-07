#Yusuf Ismaeel and Drew Child
#Homework 11 Problem 2
#Copied HW 10 Pr2

import random
"""Copying the codes from the  HW"""
def inarow_Neast(ch, r_start, c_start, A, N):
    """East equality checker for choice repeating n times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False

    if c_start > NC - N:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """South Equality Checker for input repeated N times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start > NR-N:
        return False

    if c_start > NC:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """SouthEast Equality checker for the choice n times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start > NR-N:
        return False

    if c_start > NC - N:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True

def inarow_Nnortheast(ch,r_start, c_start, A, N):
    """Equality checker for going northeast for the choice repeating N times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >NR:
        return False
    if c_start > NC:
        return False
    if NC-c_start<N:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start-i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox): 
        """Adds a move to the given column"""
        for i in range(self.height):
            if self.data[self.height-i-1][col] == ' ':
                self.data[self.height-i-1][col] = ox
                return
    
    def clear(self):
        """removes all x's and o's from the board to return a brand new one"""
        for x in range(self.height):
            for y in range(self.width):
                self.data[x][y] = ' '
    
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    
    def allowsMove(self,c):
        """A function that checks if this move is permissible in connet four or not"""
        if c<0 or c>= self.width:
            return False
        if self.data[0][c]!= ' ':
            return False
        return True

    def isFull(self):
        """A function that checks if the board is full or not"""
        for x in range(self.width):
            if self.allowsMove(x):
                return False
        return True

    def delMove(self,c):
        """Deletes a move from the board"""
        for x in range(self.height):
            if self.data[x][c] == 'X' or self.data[x][c]== 'O':
                self.data[x][c]= ' '
                return
    
    def winsFor(self,ox):
        """Checker for which option wins"""
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox,row,col,D,4):
                    return True
                if inarow_Nnortheast(ox,row,col,D,4):
                    return True
                if inarow_Nsouth(ox,row,col,D,4):
                    return True
                if inarow_Nsoutheast(ox,row,col,D,4):
                    return True
        return False

    
    def hostGame(self):
        """This starts a game of Connect Four!"""
        print("Welcome to the intense game of Connect 4!")
        print(self)
        while True:
            Human_col = -1
            while not self.allowsMove(Human_col):
                Human_col = int(input("User, Choose a column: "))
            self.addMove(Human_col,'X')
            print(self)
            if self.winsFor("X"):
                print("User Wins!")
                print(self)
                response = input("Care to play Again? Y/N ")
                if response == 'Y':
                    hostGame(self)
                else:
                    break
           # comps_col = -1 this is not needed but I had though I'd need it
            compMove = int(self.aiMove('O'))
            self.addMove(compMove,'O')
            print(self)
            if self.winsFor('O'):
                print("Computer Wins!")
                print(self)
                response = input("Care to play Again? Y/N ")
                if response == 'Y':
                    hostGame(self)
                else:
                    break
            elif self.isFull:
                print("A gentleman's tie!")
                break
    def colsToWin(self, ox):
        """This is a function that tells you which  columns you play in roder win the game"""
        winningList= []
        for column in range(self.width):  #checks the columns
            if self.allowsMove(column):   #checks if the given column is usable (playable)
                self.addMove(column,ox)   #if it's playable you add the move to the column
            if self.winsFor(ox):          #now checks if the previous move in the column wins
                winningList.append(column) #if so, we append our winning list
            self.delMove(column)           #we that move from the column in order to recheck and not double count moves!
        return winningList                 #returns the list of columns that could win you the game

    def aiMove(self, ox):
        """this is the artificial intelligence's move"""
        #Going to assume that aiMove is the computer itself and it chooses between o or x
        if ox == 'X':
            Human = 'O'
        else:
            Human = 'X'
        aiWin = self.colsToWin(ox)
        humanWin = self.colsToWin(Human)
        if aiWin != []: #checks if there are any columns that the AI can win by playing
            aiMove = aiWin[0]  #if so, it plays the column
        else:
            if humanWin!= []:  #if the AI cannot win this column, the AI checks for ways of preventing the opposition from winning
                aiMove = humanWin[0]  #blocks a column that makes the opposition from winning
            else:
                if self.allowsMove(random.choice(range(self.width))):    #chooses a random spot to play the base, if it works it plays it there
                    aiMove= random.choice(self.width)
                else:
                    aiMove = random.choice(aiWin)                        #else, it chooses another spot that will further help it win the game later on!
        return aiMove
            
    