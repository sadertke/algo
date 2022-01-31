n  = int(input())
t = [0 for i in range(n)]
p = [0 for i in range(n)]



for i in range(n) :
    ti,pi = map(int, input().split())
    t[i] = ti
    p[i] = pi

m = []
#구간 그래프 만들기 ex)시작 끝 [0, 2]
for i in range(n) :
    
    if i+t[i]-1<n :
        m.append([i,i+t[i]-1,p[i]])
    p[i]=-1

m.sort(key= lambda p: p[1])


maxs =-1  
            
def dfs(m,num,n2) :
    #print(m)
    lis =[]
    s =0
    maxs =-1
    
    if num==1 and m[0][1]<n2:
        #print(m)
        return m[0][2]

    elif num==1 or num==0 :
        return 0
    
    for i in range(num) :
        end = m[i][1]
        s = m[i][2]
        #print(s)
        for j in range(i+1,num) :
            if m[j][0]<= end :
                continue
            else :
                lis.append(m[j])

        
        if lis is not None :
            if p[m[i][0]] >=0 :
                s= p[m[i][0]]
            else :
                p[m[i][0]] = s+dfs(lis,len(lis),n2)
                s= p[m[i][0]]
                
            maxs =max(maxs,s)
            p[m[i][0]] = max(maxs,p[m[i][0]])

            lis =[]
        else :
            if p[m[i][0]] >=0 :
                s= p[m[i][0]]
            else :
                p[m[i][0]] = s
                
            
            maxs =max(maxs,s)
            p[m[i][0]] = max(maxs,p[m[i][0]])
            
              

    return maxs
print(dfs(m,len(m),n))      
    
