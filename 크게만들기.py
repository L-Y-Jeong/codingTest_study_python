N, K = map(int, input().split())
arr = list(input())
stack = []

for n in arr:
    while stack and stack[-1] < n and K > 0:
        stack.pop()
        K -= 1
    stack.append(n)

if K == 0:
    print(''.join(stack))
else:
    print(''.join(stack[:-K]))
