#author: MJ
#2020-01-18

from random import randint
import math

"""
Magic Squares:
A n*n square of the numbers 1,2,3...n^2 is built up. The square is told to be 'magic'
if all rows, columns and diagonals add up to the same number. For instance,
the following:
-----------
16,3,2,13,
5,10,11,8,
9,6,7,12,
4,15,14,1
-----------
is magic, for n = 4. If you switch e.g. the numbers 2 <-> 3, the two middle columns are flawed.

This program is to take a number sequence s (by user input or randomising function) of size n*n
as input. Thereafter, it will check whether s forms a magic square. 
"""

#----------MAIN----------#

def main():
    equalityReached = False
    while equalityReached == False:
        print("\nNEW SQUARE:")
        game = Game(3)
        game.randomNrSeqIsGenerated()
        print(game.inputArray)
        game.sortIntoRows()
        game.sortIntoCols()
        game.sortIntoDiagonals()

        if game.sumsAreEqual() == True:
            equalityReached = True
            game.illustrateMagicSquare()
    print("Done!")


#----------GAME CLASS----------#

class Game:
    'the game object'

    def __init__(self,side):
        self.side = side
        self.size = side**2
        self.inputArray = []
        self.totalArray = []
    
    def getInputArray(self): return self.inputArray

    def randomNrSeqIsGenerated(self):
        arr = [i for i in range(1,self.size+1)]
        
        #The numbers in arr is now to be randomly put into another array.
        #A replica of the built-in 'Shuffle' function
        while len(arr) > 0:
            i = randint(0,len(arr)-1)
            self.inputArray.append(arr[i])
            arr.pop(i)
    
    def sortIntoRows(self):
        i = 0
        copyOfInputArray = self.inputArray[:]
        while i < self.size:
            rowArray = []
            for _ in range(self.side):
                rowArray.append(copyOfInputArray[0])
                copyOfInputArray.pop(0)
            self.totalArray.append(rowArray)
            i += self.side
    
    def sortIntoCols(self):
        copyOfInputArray = self.inputArray[:]
        for i in range(self.side):
            colArray = []
            n = i
            while n < self.size:
                colArray.append(copyOfInputArray[n])
                n += self.side
            self.totalArray.append(colArray)

    
    def sortIntoDiagonals(self):
        copyOfInputArray = self.inputArray[:]
        #1
        n = 0
        add = 0
        diagonal1 = []
        diagonal2 = []
        for _ in range(self.side):
            diagonal1.append(copyOfInputArray[n+add])
            add += 1
            n += self.side
        self.totalArray.append(diagonal1)
        n = self.size-self.side
        add = 0
        for _ in range(self.side):
            diagonal2.append(copyOfInputArray[n+add])
            add += 1
            n -= self.side
        self.totalArray.append(diagonal2)
        print(self.totalArray)

    def sumsAreEqual(self):
        theSum = sum(self.totalArray[0])
        equal = True
        i = 1
        while i < len(self.totalArray):
            if theSum != sum(self.totalArray[i-1]):
                equal = False
            i += 1
        if equal == True:
            print("\nEqual!")
            for n in self.totalArray:
                print(n)
        else:
            print("Non-magic... :/")
        return equal
    
    def illustrateMagicSquare(self):
        print("\nThe Magic Square:\n")
        self.horiz()
        for i in range(self.side):
            string = ''
            for n in range(len(self.totalArray[i])):
                string = string + ' | ' + str(self.totalArray[i][n])
            print(string + ' |')
            self.horiz()

    def horiz(self):
        line = ' +'
        for _ in range(self.side):
            line = line + '---+'
        print(line)










if __name__ == "__main__":
    main()