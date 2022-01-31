
num  = int(input())
A = list(map(int,input().split()))
rtn =[]
rtn.append(A[0])
for i in A :
    if i>rtn[-1] :
        rtn.append(i)
    else :
        l = 0
        h = len(rtn)-1
        mid = (l + h) // 2
        while h>l :
            mid = (l + h) // 2
            if rtn[mid]< i :
                l =  mid+1
            else :
                h = mid
        rtn[l] = i

print(len(rtn))
