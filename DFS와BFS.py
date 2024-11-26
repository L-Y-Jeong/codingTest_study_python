
from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

# 정보입력
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

# dfs
dfs_visited = [0]*(N+1)

def dfs(V):
    dfs_visited[V] = 1
    print(V, end=' ')
    for j in range(1, N+1):
        if graph[V][j] == 1 and dfs_visited[j] == 0:
            dfs(j)

# bfs
bfs_visited = [0]*(N+1)

def bfs(V):
    que = deque([V])  
    bfs_visited[V] = 1
    while que:
        v = que.popleft()
        print(v, end=' ')
        for k in range(1, N+1):
            if bfs_visited[k] == 0 and graph[v][k] == 1:
                que.append(k)
                bfs_visited[k] = 1

dfs(V)
print()
bfs(V)
