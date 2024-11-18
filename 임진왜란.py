
import sys

input = sys.stdin.readline


n = int(input())

ans = dict(zip(input().split(), [i for i in range(n)]))
w = input().split()
cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if ans[w[i]] < ans[w[j]]:
            cnt += 1

print(cnt, "/", n * (n - 1) // 2, sep="")
