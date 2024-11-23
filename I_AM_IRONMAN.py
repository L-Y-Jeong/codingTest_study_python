import sys

input = sys.stdin.readline

gameN, player = map(int, input().split())

dict = {}

score = 0

w, l, g = map(int, input().split())

for _ in range(player):
    name, res = map(str, input().split())

    dict[name] = res

for _ in range(gameN):
    p = input().rstrip()

    if p not in dict or (p in dict and dict[p] == 'L'):
        score -= l
        if score < 0 :
            score = 0
    elif p in dict and dict[p] == 'W':
        score += w

    if score >= g :
        print("I AM NOT IRONMAN!!")
        break

else :
    print("I AM IRONMAN!!")

