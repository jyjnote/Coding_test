n = int(input())
p = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            p[i][j] = 1

a = 0
for r in p:
    a += r.count(1)
print(a)