#MAZE SOLVER Backtracking Approach

'''
    Input = 1. Matrix of the maze that needs to be solved
            eg - matrix = [
                [1,0,0,0],
                [1,1,0,1],
                [0,1,0,0],
                [1,1,1,1]
            ]
            2. tuple mentioning the destination co-ordinates
            eg - dest = (3,3)
'''

def isAllowed(pos,matrix):   #----> check if the position is alloweed or not
    if pos[0]<len(matrix) and pos[1]<len(matrix[0]) and pos[0]>=0 and pos[1]>=0:
        if matrix[pos[0]][pos[1]]==1:
            return True
    return False

def Solution(matrix,moves,dest,sol,pos):   #----> Finding the solution using Backtracking
    if pos == dest:
        sol[dest[0]][dest[1]]=1
        return True
    for move in moves:
        x = pos[0]+move[0]
        y = pos[1]+move[1]
        if isAllowed(pos,matrix):
            sol[pos[0]][pos[1]]=1
            flag = Solution(matrix,moves,dest,sol,(x,y))
            if flag:
                return True
    return False

def print_solution(sol):   #----> Print the final solution
    for i in sol:
        for j in i:
            print(j,end='')
        print()

def maze_solver(matrix,dest): #-----> Calling Function
    sol = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    moves = [(0,1),(1,0)]
    sol[0][0]=1
    flag = Solution(matrix,moves,dest,sol,(0,0))
    if flag:
        print_solution(sol)
    else:
        print('No possible solution')



# Main Function change values of matrix and dest to check

if __name__ == '__main__':
    matrix = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
         ]
    dest = (3,3)
    maze_solver(matrix,dest)
