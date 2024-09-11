num = int(input())
arr = list(map(int, input().split()))
stack = []
res = [-1] * num

for i in range(num):
    while stack and arr[stack[-1]] < arr[i]:
        res[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
    
print(*res)
