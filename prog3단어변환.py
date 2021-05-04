from collections import deque 
def solution(begin, target, words):
    answer = 0
    
    q = deque()
    q.append([begin,0])
    leng = len(begin)
    
    while q :
        a,c =q.popleft()
        if a==target :
            return c
        
        for word in words :
            count =0
            #현재 단어와 1개만 다른 word를 찾는다
            for i in range(leng):
                if a[i]!=word[i]:
                    count= count+1
            if count ==1 :
                #찾은걸 큐에 넣어준다 c는 변환 횟수다
                q.append([word,c+1])
                words.remove(word)
                    
                
    answer =0
    return answer
