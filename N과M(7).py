import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

num = list(map(int,input().split()))
num.sort()

def dfs():
    if len(res) == m :
        print(' '.join(map(str, res)))
        return
    
    for i in num:
        res.append(i)
        dfs()
        res.pop()

dfs()
