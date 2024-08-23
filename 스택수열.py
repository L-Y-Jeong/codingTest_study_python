
stack = []
res = []
find = 0
index = 1
n = int(input())

for _ in range(n):
    num = int(input())

    while index <= num : #push
        stack.append(index)
        res.append('+')
        index += 1

    if stack[-1] == num : #pop
        stack.pop()
        res.append('-')
    else : #안될 때
        print("NO")
        find = 1
        break
        

if find == 0 :  #불가능한 경우
    for i in res :
        print(i)


