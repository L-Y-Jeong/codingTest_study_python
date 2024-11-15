import sys

input = sys.stdin.readline

while True:
    str = input().rstrip()
    if str == "*" :
        break

    for d in range(1, len(str)-1):
        check = set()
        for i in range(len(str)-d):
            pairs = str[i]+str[i+d]
            if pairs in check:
                print(str, "is NOT surprising.")
                break
            else :
                check.add(pairs)
        else :
            continue
        break
    else :
        print(str, "is surprising.")
