#컴퓨터의 개수가 200개 까지이므로 유니온 파인드 구현을 균형을 고려하지 않았다 
arr =[i for i in range(201)]
def par(n):
    if arr[n] ==n :
        return n
    else :
        return par(arr[n])
    
def find(a,b):
    if par(a)==par(b):
        return False
    else:
        return True
def union(a,b):
    if find(a,b):
        arr[par(b)] =par(a)
    else :
        return
    
def solution(n, computers):
    
    answer =0
    
    for i in range(n-1):
        for j in range(i+1,n):
            if computers[i][j]==1:
                union(i,j)
                
    for i in range(n):
        if i == arr[i]:
            answer=answer+1
    
    return answer
