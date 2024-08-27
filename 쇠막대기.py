stack=[]
cnt = 0

arr = input()

for i in range(len(arr)):
    if arr[i] == '(': #열린 괄호
        stack.append(arr[i])
    else : # 닫힌 괄호
        stack.pop()
        if arr[i-1] == '(': #레이저일 때
            cnt += len(stack) 
        else : #쇠막대기 끝부분
            cnt+= 1
print(cnt)
