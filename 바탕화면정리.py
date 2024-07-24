def solution(wallpaper):
    answer = []
    
    x, y = 0, 0
    w = len(wallpaper[0]) #열
    h = len(wallpaper) #행
    
    minX = w #시작점x
    minY = h #시작점y
    
    maxX = 0 #끝점x
    maxY = 0 #끝점y
    
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                if (minX > i):
                    minX = i
                if (minY > j):
                    minY = j
                if (maxX < i):
                    maxX = i
                if (maxY < j):
                    maxY = j
    
    maxX += 1
    maxY += 1
    
    return minX, minY, maxX, maxY
