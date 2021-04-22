n = int(input())

b = [ 0 for i in range(n+1)]

count = 0

def p(num) :
    for i in range(num) :
        if b[num]==b[i] or ((num-i) == abs(b[num]-b[i])) :
            return False

    return True
    
    
def nq(num) :
    global count 
    if num==n:
        count+=1
        
    for i in range(n):
        b[num] = i
        if p(num) :
            nq(num+1)

nq(0)
print(count)
        
    
