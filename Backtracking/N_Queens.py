#N QUEENS
def isAllowed(row,col,sol,N):
    for curr_row in range(N):
        if sol[curr_row][col]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,N,+1)):
        if sol[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if sol[i][j]==1:
            return False
    return True

def Solution(sol,N,row):
    if row == N:
        return True
    for col in range(N):
        if isAllowed(row,col,sol,N):
            sol[row][col]=1
#             print_solution(sol)
            flag = Solution(sol,N,row+1)
            if flag:
                return True
            sol[row][col]=0
    return False

def print_solution(sol):
    for i in sol:
        for j in i:
            print(j,end=' ')
        print()
    print()
def n_queens(N):
    N = int(N)
    sol = [[0 for i in range(N)] for j in range(N)]
    col = 0
    flag = Solution(sol,N,0)
    if flag:
        print_solution(sol)
    else:
        print('No possible solution')

if __name__ == '__main__':
    n_queens(input())