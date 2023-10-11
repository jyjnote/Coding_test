
from collections import deque
n=int(input())
a=[i for i in range(1,n+1)]
a=deque(a)

an=[]
while 1:
    an.append(a.popleft())
    a.rotate(-1)
    if len(a)==0:
        break
print(*an)