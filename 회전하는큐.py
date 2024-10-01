from collections import deque

leng, n = map(int, input().split())
que = deque()
for i in range(1, leng+1):
    que.append(i)

cnt = 0

tar = list(map(int, input().split()))

for t in tar:
    while(True):
        if que[0] == t :
            que.popleft()
            break
        else :
            if len(que)//2 < que.index(t):
                que.rotate(1)
                cnt += 1
            else :
                que.rotate(-1)
                cnt += 1

print(cnt)

