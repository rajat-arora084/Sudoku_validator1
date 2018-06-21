'''
Created on Jun 21, 2018

@author: rajat.arora07
'''


#Call the function sudoku2 with the sudoku matrix.
#Given spaces in sudoku matrix as '.' (dot)

def sudoku3(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #print i,j,grid[i][j]
            if(grid[i][j]!='.'):
                j_check=j+1
                while(j_check<len(grid[0])):
                    #print 'check in j',j_check,grid[i][j_check]
                    if(grid[i][j_check]==grid[i][j]):
                        return False
                    j_check+=1
                i_check=i+1
                while(i_check<len(grid)):
                    #print 'check in i',i_check,grid[i_check][j]
                    if(grid[i_check][j]==grid[i][j]):
                        return False
                    i_check+=1
                    
    return True

def sudoku2(grid):
    if(sudoku3(grid)==False):
        return False
    l1=[]
    for i in range(3):
        for j in range(3):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        return False
    l1=[]
    for i in range(3):
        for j in range(3,6):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        #pass
        return False
    l1=[]
    for i in range(3):
        for j in range(6,9):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        return False
    l1=[]
    for i in range(3,6):
        for j in range(3):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        #pass
        return False
    l1=[]
    for i in range(3,6):
        for j in range(3,6):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        #pass
        return False
    l1=[]
    for i in range(3,6):
        for j in range(6,9):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        #pass
        return False
    l1=[]
    for i in range(6,9):
        for j in range(3):
            l1+=[grid[i][j]]
    #print l1
    
    if(sudoku3(l1)==False):
        #pass
        return False
    l1=[]
    for i in range(6,9):
        for j in range(3,6):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        #pass
        return False
    l1=[]
    for i in range(6,9):
        for j in range(6,9):
            l1+=[grid[i][j]]
    #print l1
    if(sudoku3(l1)==False):
        return False
    return True
