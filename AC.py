from collections import deque

num = int(input())

for tc in range(num):
    cmd = input()
    arrN = int(input())

    que = deque(input()[1:-1].split(','))
    flag = 0

    if arrN == 0:  
        que = []
    
    for c in cmd:
        if c == 'R':
            flag += 1
        elif c == 'D':
            if len(que) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    que.pop()
                else:
                    que.popleft()
                        
    else:
        if flag % 2 == 1:
            que.reverse()
        print('[' + ','.join(que) + ']')
