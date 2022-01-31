

n,m,x,y,c = map(int,input().split())
board = []
for i in range(n) :
    board.append(list(map(int,input().split())))

comands = list(map(int,input().split()))

dice = [0 for i in range(6)]
# 주사위 위 0 동1남2서3북4 밑 5
# c4     위 4 동1남0서3북5 밑 2

d = [[0,1],[0,-1],[-1,0],[1,0]]

for i  in range(c) :
    if 0<=(x+d[comands[i]-1][0])<n and 0<=(y+d[comands[i]-1][1])<m:
        x+=d[comands[i]-1][0]
        y+=d[comands[i]-1][1]
        
        if comands[i] ==4 :
            temp = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = dice[2]
            dice[2] = temp
        elif comands[i] ==3 :
            temp = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = dice[4]
            dice[4] = temp
        elif comands[i] ==1 :
            temp = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = dice[1]
            dice[1] = temp
        elif comands[i] ==2 :
            temp = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[3]
            dice[3] = temp
        print(dice[0])
        if board[x][y] ==0 :
            board[x][y] = dice[5]
        else :
            dice[5] = board[x][y]
            board[x][y] =0

        
            
            
