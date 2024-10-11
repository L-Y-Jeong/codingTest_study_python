from collections import deque

n, k = map(int, input().split())

que = deque(range (1, n+1))

res = []
while que:
    que.rotate(-k+1)
    res.append(que.popleft())

print('<'+ ', '.join(map(str, res)) +'>')
