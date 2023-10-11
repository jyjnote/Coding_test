from collections import deque

n, k = map(int, input().split())

r = []

c = deque(range(1, n + 1))

while c:

    c.rotate(-k + 1)
    r.append(c.popleft())

print("<" + ", ".join(map(str, r)) + ">")
