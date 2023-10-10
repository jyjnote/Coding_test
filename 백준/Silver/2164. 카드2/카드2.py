from collections import deque

a = int(input())
b = deque(range(1, a + 1))

while len(b) > 1:
    b.popleft()
    b.rotate(-1)

print(b[0])
