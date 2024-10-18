import heapq
import sys

input = sys.stdin.readline
n = int(input().strip())

heap = []

for _ in range(n):
    x = int(input().strip())    
    if x == 0 :
        if not heap :
            print(0)
        else :
            print(heapq.heappop(heap)[1])
    else :
        heapq.heappush(heap, (abs(x), x))
