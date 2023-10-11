from collections import deque
import sys

d = deque()
n = int(input())

for i in range(n):
    c, *args = sys.stdin.readline().split()

    if c == "push_front":
        d.appendleft(args[0])
    elif c == "push_back":
        d.append(args[0])
    elif c == "pop_front":
        if d:
            print(d[0])    
            d.popleft()
        else:
            print("-1")
    elif c == "pop_back":
        if d:
            print(d[-1])    
            d.pop()
        else:
            print("-1")
    elif c == "size":
        print(len(d))
    elif c == "empty":
        print(0 if d else 1)
    elif c == "front":
        print(d[0] if d else -1)
    elif c == "back":
        print(d[-1] if d else -1)
