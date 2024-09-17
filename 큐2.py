
import sys
from collections import deque

que = deque()

for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        que.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(-1 if not que else que.popleft())
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        print(1 if not que else 0)
    elif cmd[0] == "front":
        print(-1 if not que else que[0])
    elif cmd[0] == "back":
        print(-1 if not que else que[-1])
