#Sum of subset

def Solution(array,dest,length,temp_sum,sol,index):
    if temp_sum == dest:
        return True
    
    for i in range(index,length,1):
#         print(array[i],end='->')
#         print_solution(array,sol)
        if temp_sum + array[index]<=dest:
            sol[i]=1
            index = i
#             print(sol)
            flag = Solution(array,dest,length,temp_sum+array[index],sol,index+1)
            if flag:
                return True
            sol[i]=0
    return False

def print_solution(array,sol):
    for i in range(len(array)):
        if sol[i]==1:
            print(array[i],end=' ')
    print()

def sum_of_subset(array,dest):
    length = len(array)
    temp_sum=0
    sol = [0 for i in range(length)]
    flag = Solution(array,dest,length,temp_sum,sol,index=0)
    if flag:
        print_solution(array,sol)
    else:
        print("No solution found")

if __name__ == '__main__':
    array = [2,4,2,6,3,5]
    dest = 10
    sum_of_subset(array,dest)