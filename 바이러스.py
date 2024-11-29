
from collections import deque
import sys

input = sys.stdin.readline

# N = 정점 개수, M = 간선 개수, V = 시작할 정점 번호
N = int(input())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0]*(N+1)
cnt = 0

def bfs(V):
    que = deque([V])  
    visited[V] = 1
    cnt = 0
    while que:
        v = que.popleft()
        cnt += 1
        for j in range(1, N+1):
            if visited[j] == 0 and graph[v][j] == 1:
                que.append(j)
                visited[j] = 1


    print(cnt-1)
bfs(1)
