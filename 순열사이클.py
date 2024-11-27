import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            stack = [i]

            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = 1
                    stack.append(arr[node])

            cnt += 1

    print(cnt)
