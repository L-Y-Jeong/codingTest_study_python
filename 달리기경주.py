def solution(players, callings):  
    n = len(callings)
    for i in range(n):
        name = callings[i] # callings 이름
        num = players.index(name) #같은 이름의 위치 찾음
        tmp = players[num]
        players[num] = players[num-1]
        players[num-1] = tmp
    
   
    return players
