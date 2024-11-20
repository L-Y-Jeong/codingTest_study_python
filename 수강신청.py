import sys
import operator

input = sys.stdin.readline

k, l = map(int, input().split())
numDict = {}

for i in range(l):
    studentNum = input().rstrip()

    numDict[studentNum] = i

sortNum = sorted(numDict.items(), key = operator.itemgetter(1))

for j in range(k):
    if j < len(sortNum):
        print(sortNum[j][0])
    else:
        break
