def check() :
    stack = []
    arr = input()
    arrN = len(arr)
    for j in range(arrN):
        if (arr[j] == '('):
            stack.append(1)
        elif (arr[j] == ')'):
            if not stack:
                return "NO"
            stack.pop()
        
                
    if stack :
         return "NO"
    elif not stack :
         return "YES"

def main():
    num = int(input())
    for i in range(num):
        result = check()
        print(result)

main()
