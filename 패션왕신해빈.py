import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    clothes = {}
    res = 1
    n = int(input())

    for _ in range(n):
        name, type = input().rstrip().split()

        if not type in clothes : 
            clothes[type] = 1
        else :
            clothes[type] += 1

    
    for i in clothes :
        res *= (clothes[i] + 1)

    print(res - 1)
