from collections import deque


testcase = int(input())
arr = []

for _ in range(testcase):
  n, m = map(int, input().split())
  arr = list(enumerate(list(map(int, input().split()))))
  x = arr[m]
  index = 0

  while len(arr):
    xMax = max([i[1] for i in arr])
    if arr[0][1] == xMax:
      y = arr.pop(0)
      index += 1
      if y == x:
        print(index)
        break
    else:
      y = arr.pop(0)
      arr.append(y)
