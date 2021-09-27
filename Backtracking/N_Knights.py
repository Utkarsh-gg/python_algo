def isVisited(x,y,board,n):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if board[x][y]==-1:
        return True
    return False

def Solution(board,moves,pos,curr_x,curr_y,n):

    if(pos == n**2):
        return True
    
    for i in moves:
        x = curr_x + i[0]
        y = curr_y + i[1]
        if (isVisited(x,y,board,n)):
            board[x][y]=pos
            # print_solution(board,n)
            flag=Solution(board,moves,pos+1,x,y,n)
            if flag:
                return True
            board[x][y]=-1
    return False


def print_solution(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print(' ')
    print(' ')

def Knight(n):
    board = [[-1 for i in range(n)]for j in range(n)]
    moves = [(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(-1,2),(-2,1),(2,-1)]
    pos = 1
    board[0][0]=0
    curr_x=0
    curr_y=0
    flag = Solution(board,moves,pos,curr_x,curr_y,n)
    if flag:
        print_solution(board,n)
    else:
        print('Solution does not exist')

if __name__ == '__main__':
    Knight(7)