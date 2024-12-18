import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int,input().split())))

res = []

def dfs(start):
    if len(res) == m:
        print(*res)
        return

    for i in range(start,n):
        res.append(arr[i])
        dfs(i+1)
        res.pop()

dfs(0)
