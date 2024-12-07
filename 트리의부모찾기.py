
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) #재귀 리미트 (이거 없으니까 런타임 에러 뜸)

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    # graph[x].append(y) #메모리 초과이슈로 graph[x][y] = 1 로 하면 안된다네
    # graph[y].append(x)
    graph[x][y] = graph[y][x] = 1
visited = [0] * (N+1)


def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v # 1이 아니라 부모노드인 v를 저장
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])
