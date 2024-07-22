def solution(park, routes):
    answer = []
    
    x, y = 0, 0
    w = len(park[0]) #행 개수
    h = len(park) #열 개수
    opn = {"E":(0,1), "W":(0,-1), "S":(1,0), "N":(-1,0)}
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i #시작점 열 위치
                y = j #시작점 행 위치
                break
            
            
    for i in routes:
        v, d = i.split(" ") #방향, 거리
        dx, dy = x, y #지금 있는 위치
            
        for j in range(int(d)):
            numX = x + opn[v][0] #이동
            numY = y + opn[v][1]
                
            if (0<=numX<=h-1) and (0<=numY<=w-1) and (park[numX][numY]!="X") :
                x, y = numX, numY
            else:
                x, y = dx, dy
                break
                    
    answer = (x,y)
    return answer
