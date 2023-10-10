from collections import deque
import sys

n = int(input())
q = deque()

for _ in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        q.append(int(c[1]))
    elif c[0] == 'pop':
        print(q.popleft() if q else -1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        print(0 if q else 1)
    elif c[0] == 'front':
        print(q[0] if q else -1)
    elif c[0] == 'back':
        print(q[-1] if q else -1)
